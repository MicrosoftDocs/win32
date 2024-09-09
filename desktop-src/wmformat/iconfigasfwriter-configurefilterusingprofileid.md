---
title: IConfigAsfWriter ConfigureFilterUsingProfileId method
description: The ConfigureFilterUsingProfileId method configures the filter to write an ASF file with a profile identifier (ID) index from the system profile list. (For Windows Media Format 4.0 profiles only.).
ms.assetid: b0375785-83db-4540-aca9-7ba0bb81c1ef
keywords:
- ConfigureFilterUsingProfileId method windows Media Format
- ConfigureFilterUsingProfileId method windows Media Format , IConfigAsfWriter interface
- IConfigAsfWriter interface windows Media Format , ConfigureFilterUsingProfileId method
topic_type:
- apiref
api_name:
- IConfigAsfWriter.ConfigureFilterUsingProfileId
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# IConfigAsfWriter::ConfigureFilterUsingProfileId method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **ConfigureFilterUsingProfileId** method configures the filter to write an ASF file with a profile identifier (ID) index from the system profile list. (For Windows Media Format 4.0 profiles only.)

## Syntax


```C++
HRESULT ConfigureFilterUsingProfileId(
  [in] DWORD dwProfileId
);
```



## Parameters

<dl> <dt>

*dwProfileId* \[in\]
</dt> <dd>

Profile ID as defined in version 4.0 of the Windows Media Format SDK.

</dd> </dl>

## Return value

Returns one of the following **HRESULT** values.



| Return code                                                                                         | Description                             |
|-----------------------------------------------------------------------------------------------------|-----------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                | The method succeeded.<br/>        |
| <dl> <dt>**E\_FAIL**</dt> </dl>              | The profile is not valid.<br/>    |
| <dl> <dt>**VFW\_E\_WRONG\_STATE**</dt> </dl> | The filter graph is stopped.<br/> |



 

## Remarks

This method is now obsolete because it assumes version 4.0 Windows Media Format SDK profiles. To configure the filter for version 7.0 and later profiles, use [**IConfigAsfWriter::ConfigureFilterUsingProfile**](iconfigasfwriter-configurefilterusingprofile.md) or [**IConfigAsfWriter::ConfigureFilterUsingProfileGuid**](iconfigasfwriter-configurefilterusingprofileguid.md).

## See also

<dl> <dt>

[**IConfigAsfWriter Interface**](/previous-versions/windows/desktop/legacy/dd743205(v=vs.85))
</dt> </dl>

 

