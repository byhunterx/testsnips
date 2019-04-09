import webbrowser
if len(intentMessage.slots.pdts) > 0:
   val = intentMessage.slots.pdts.first().rawValue
   url = "http://360.topnegoce.com:8000/new/admin/R_Banc_ass/php/SNIPS_ASSET/response.php?intent=pr&val="+val
   webbrowser.open_new_tab(url)
