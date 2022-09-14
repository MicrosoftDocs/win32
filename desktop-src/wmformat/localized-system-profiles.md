---
title: Localized System Profiles
description: Localized System Profiles
ms.assetid: 2c218ab4-ecdb-414c-aa42-b71a42e340e5
keywords:
- Windows Media Format SDK,system profiles
- Advanced Systems Format (ASF),system profiles
- ASF (Advanced Systems Format),system profiles
- Windows Media Format SDK,localized system profiles
- Advanced Systems Format (ASF),localized system profiles
- ASF (Advanced Systems Format),localized system profiles
- system profiles,localized
- localized system profiles,list of
ms.topic: article
ms.date: 05/31/2018
---

# Localized System Profiles

The following table lists the localized system profile files included with the Windows Media Format SDK and the languages associated with each. These files are installed into the \[SDKRoot\]\\WMSDK\\WMFSDK9\\LocalizedProfiles folder. To access a particular file with the **IWMProfileManagerLanguage** methods, you must move it into the system root directory along with the default system profile files.



| Language              | File name    |
|-----------------------|--------------|
| Arabic                | WMPrfAra.prx |
| Chinese – simplified  | WMPrfCHS.prx |
| Chinese – traditional | WMPrfCHT.prx |
| Czech                 | WMPrfCsy.prx |
| Danish                | WMPrfDan.prx |
| Dutch                 | WMPrfNld.prx |
| Finnish               | WMPrfFin.prx |
| French                | WMPrfFra.prx |
| German                | WMPrfDeu.prx |
| Greek                 | WMPrfEll.prx |
| Hebrew                | WMPrfHeb.prx |
| Hungarian             | WMPrfHun.prx |
| Italian               | WMPrfIta.prx |
| Japanese              | WMPrfJpn.prx |
| Korean                | WMPrfKor.prx |
| Norwegian             | WMPrfNor.prx |
| Polish                | WMPrfPlk.prx |
| Portuguese – Brazil   | WMPrfPtb.prx |
| Portuguese – Portugal | WMPrfPtg.prx |
| Russian               | WMPrfRus.prx |
| Slovak                | WMPrfSky.prx |
| Slovenian             | WMPrfSlv.prx |
| Spanish               | WMPrfEsp.prx |
| Swedish               | WMPrfSve.prx |
| Turkish               | WMPrfTrk.prx |



 

You can set the language for the profile manager object by calling the [**IWMProfileManagerLanguage::SetUserLanguageID**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofilemanagerlanguage-setuserlanguageid) method. For most languages, only the primary language identifier in the LANGID is examined. The exceptions are for the Chinese and Portuguese languages, where the secondary language identifier is also used. The following table shows how to create a LANGID to specify in the **SetUserLanguageID** method.



| Primary-secondary language | MAKELANGID Macro                                             |
|----------------------------|--------------------------------------------------------------|
| Chinese (simplified)       | MAKELANGID( LANG\_CHINESE, SUBLANG\_CHINESE\_SIMPLIFIED)     |
| Chinese (traditional)      | MAKELANGID( LANG\_CHINESE, SUBLANG\_CHINESE\_SINGAPORE)      |
| Portuguese (Brazil)        | MAKELANGID(LANG\_PORTUGUESE, SUBLANG\_PORTUGUESE\_BRAZILIAN) |
| Portuguese (Portugal)      | MAKELANGID(LANG\_PORTUGUESE, SUBLANG\_PORTUGUESE)            |



 

## Related topics

<dl> <dt>

[**Programming Reference**](programming-reference.md)
</dt> <dt>

[**System Profiles**](system-profiles.md)
</dt> </dl>

 

 




