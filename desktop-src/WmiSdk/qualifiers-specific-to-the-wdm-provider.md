---
description: The following qualifiers are used by the WDM Provider in device driver MOF files when they are extracting data from WNODEs to generate instances of WDM driver classes.
ms.assetid: 11b0af59-979f-4908-baef-c9ec564b3cfd
ms.tgt_platform: multiple
title: Qualifiers Specific to the WDM Provider
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Qualifiers
api_type: 
- NA
api_location: 
---

# Qualifiers Specific to the WDM Provider

The following qualifiers are used by the [WDM Provider](/windows/desktop/WmiCoreProv/wdm-provider) in device driver MOF files when they are extracting data from WNODEs to generate instances of WDM driver classes.

<dt>

<span id="MissingValue"></span><span id="missingvalue"></span><span id="MISSINGVALUE"></span>**MissingValue**
</dt> <dd>

Data type: **DWORD, array, uint8, uint16, uint32, sint8, sint16, or sint32.**

Applies to: properties

A missing value for this property should be represented by **NULL** rather than 0 (zero).

</dd> <dt>

<span id="WMIDataId"></span><span id="wmidataid"></span><span id="WMIDATAID"></span>**WMIDataId**
</dt> <dd>

Data type: **uint32**

Applies to: properties

Index in the WNODE of the data for the property. The WDM provider uses this qualifier to determine how the data is formatted while extracting data from the WNODE and generating WMI classes. The starting value is 1.

</dd> <dt>

<span id="WMIExpense"></span><span id="wmiexpense"></span><span id="WMIEXPENSE"></span>**WMIExpense**
</dt> <dd>

Data type: **uint32**

Applies to: classes

Indication of the resource cost to access the data block. For example, disk geometry information does not require a lot of resources to obtain because it is available in the device extension. Disk read/write performance is more resource-intensive because it requires extra work on each read/write operation. Therefore, the **WMIExpense** qualifier value is larger for disk read/write performance.

</dd> <dt>

<span id="WMIMethodId"></span><span id="wmimethodid"></span><span id="WMIMETHODID"></span>**WMIMethodId**
</dt> <dd>

Data type: **uint32**

Applies to: methods

Index in the WNODE of the data for the property. The WDM provider uses this qualifier to determine how the data is formatted while extracting data from the WNODE and generating WMI classes. The starting value is 1.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |



 

