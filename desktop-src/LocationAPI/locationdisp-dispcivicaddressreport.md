---
Description: Represents a civic address report.
ms.assetid: 7c6e790f-0150-4ea8-9583-df633ebf035d
title: LocationDisp.DispCivicAddressReport object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# LocationDisp.DispCivicAddressReport object

\[The Location API object model is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, to access location from a website, use the [W3C Geolocation API](https://msdn.microsoft.com/library/gg589513). To access location from a desktop application, use the [**Windows.Devices.Geolocation**](https://msdn.microsoft.com/library/windows/apps/br225603) API.\]

Represents a civic address report.

## Members

The **LocationDisp.DispCivicAddressReport** object has these types of members:

-   [Properties](#properties)

### Properties

The **LocationDisp.DispCivicAddressReport** object has these properties.



| Property                                                                              | Access type          | Description                                                 |
|:--------------------------------------------------------------------------------------|:---------------------|:------------------------------------------------------------|
| [**AddressLine1**](locationdisp-dispcivicaddressreport-addressline1.md)<br/>   | Read-only<br/> | The first line of a street address.<br/>              |
| [**AddressLine2**](locationdisp-dispcivicaddressreport-addressline2.md)<br/>   | Read-only<br/> | The second line of a street address.<br/>             |
| [**City**](locationdisp-dispcivicaddressreport-city.md)<br/>                   | Read-only<br/> | The city name.<br/>                                   |
| [**CountryRegion**](locationdisp-civicaddressreport-countryregion.md)<br/>     | Read-only<br/> | The country or region name.<br/>                      |
| [**DetailLevel**](locationdisp-dispcivicaddressreport-detaillevel.md)<br/>     | Read-only<br/> | The detail level for the report.<br/>                 |
| [**PostalCode**](locationdisp-dispcivicaddressreport-postalcode.md)<br/>       | Read-only<br/> | The postal code.<br/>                                 |
| [**StateProvince**](locationdisp-dispcivicaddressreport-stateprovince.md)<br/> | Read-only<br/> | The state or province name.<br/>                      |
| [**Timestamp**](locationdisp-dispcivicaddressreport-timestamp.md)<br/>         | Read-only<br/> | The date and time when the report was generated.<br/> |



 

## Remarks

You can retrieve this object through the [**CivicAddressReport**](locationdisp-dispcivicaddressreport-civicaddressreport.md) property of a [**CivicAddressReportFactory**](locationdisp-civicaddressreportfactory.md) object. You can receive this object through the [**NewCivicAddressReport**](newcivicaddressreport.md) event.

## Requirements



|                                     |                                            |
|-------------------------------------|--------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                  |



 

 




