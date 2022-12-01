from sunpy.net import Fido
from sunpy.net import attrs as a

event_type = "FL"
tstart = "2010/4/30"
tend = "2022/10/31"
result = Fido.search(a.Time(tstart, tend),
                     a.hek.EventType(event_type),
                     a.hek.FL.GOESCls > "C1.0",
                     a.hek.OBS.Observatory == "GOES")

hek_results = result["hek"]

new_table = hek_results["event_starttime", "event_peaktime",
                        "event_endtime", "fl_goescls", "ar_noaanum"]

new_table.write(">C1_flares.csv", format="csv")
print(len(new_table))
