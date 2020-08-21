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
ms.date: 05/31/2018
api_location: 
---

# IConfigAsfWriter::ConfigureFilterUsingProfileId method

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

 

