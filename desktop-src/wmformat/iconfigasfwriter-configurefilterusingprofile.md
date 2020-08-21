---
title: IConfigAsfWriter ConfigureFilterUsingProfile method
description: The ConfigureFilterUsingProfile method is the recommended way to set a profile. It configures the filter to write an ASF file based on the specified application-defined profile.
ms.assetid: 278e5109-ba22-4a1c-9c6a-5cfcb9f57d37
keywords:
- ConfigureFilterUsingProfile method windows Media Format
- ConfigureFilterUsingProfile method windows Media Format , IConfigAsfWriter interface
- IConfigAsfWriter interface windows Media Format , ConfigureFilterUsingProfile method
topic_type:
- apiref
api_name:
- IConfigAsfWriter.ConfigureFilterUsingProfile
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IConfigAsfWriter::ConfigureFilterUsingProfile method

The **ConfigureFilterUsingProfile** method is the recommended way to set a profile. It configures the filter to write an ASF file based on the specified application-defined profile.

## Syntax


```C++
HRESULT ConfigureFilterUsingProfile(
  [in] IWMProfile *pProfile
);
```



## Parameters

<dl> <dt>

*pProfile* \[in\]
</dt> <dd>

Pointer to the [**IWMProfile**](iwmprofile.md) interface on the application-defined profile.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                                         | Description                                                   |
|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                | The method succeeded.<br/>                              |
| <dl> <dt>**E\_POINTER**</dt> </dl>           | The **IWMProfile** interface pointer is not valid.<br/> |
| <dl> <dt>**VFW\_E\_WRONG\_STATE**</dt> </dl> | The graph is stopped.<br/>                              |



 

## Remarks

If successful, this method will cause an **EC\_GRAPH\_CHANGED** event to be sent to the application. Use this method to configure the writer with a custom Windows Media 9 Series profile you have created (or loaded from an existing .prx file) using the methods of the Windows Media Format SDK.

## See also

<dl> <dt>

[**IConfigAsfWriter Interface**](/previous-versions/windows/desktop/legacy/dd743205(v=vs.85))
</dt> </dl>

 

