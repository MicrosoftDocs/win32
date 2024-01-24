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
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# IConfigAsfWriter::ConfigureFilterUsingProfileGuid method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

