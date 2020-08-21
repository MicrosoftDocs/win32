---
title: IConfigAsfWriter ConfigureFilterUsingProfileGuid method
description: The ConfigureFilterUsingProfileGuid method configures the filter to write an ASF file based on the specified predefined profile. (Deprecated.).
ms.assetid: 94161ee7-1b74-47af-9d77-568abe6237c3
keywords:
- ConfigureFilterUsingProfileGuid method windows Media Format
- ConfigureFilterUsingProfileGuid method windows Media Format , IConfigAsfWriter interface
- IConfigAsfWriter interface windows Media Format , ConfigureFilterUsingProfileGuid method
topic_type:
- apiref
api_name:
- IConfigAsfWriter.ConfigureFilterUsingProfileGuid
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IConfigAsfWriter::ConfigureFilterUsingProfileGuid method

The **ConfigureFilterUsingProfileGuid** method configures the filter to write an ASF file based on the specified predefined profile. (Deprecated.)

## Syntax


```C++
HRESULT ConfigureFilterUsingProfileGuid(
  [in] REFGUID guidProfile
);
```



## Parameters

<dl> <dt>

*guidProfile* \[in\]
</dt> <dd>

**GUID** identifying a profile as defined in the Windows Media Format SDK header file Wmsysprf.h.

</dd> </dl>

## Return value

Returns one of the following **HRESULT** values.



| Return code                                                                                         | Description                             |
|-----------------------------------------------------------------------------------------------------|-----------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                | The method succeeded.<br/>        |
| <dl> <dt>**E\_FAIL**</dt> </dl>              | The profile is not valid.<br/>    |
| <dl> <dt>**VFW\_E\_WRONG\_STATE**</dt> </dl> | The filter graph is stopped.<br/> |



 

## Remarks

Beginning with the Windows Media Format 9 Series SDK, no new system profiles have been defined. Only version 8 (or earlier) system profile GUIDs can be used with this method.

## See also

<dl> <dt>

[**IConfigAsfWriter Interface**](/previous-versions/windows/desktop/legacy/dd743205(v=vs.85))
</dt> </dl>

 

