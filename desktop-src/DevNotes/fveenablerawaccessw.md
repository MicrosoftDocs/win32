---
description: Enables or disables reading and writing of disk sectors.
ms.assetid: 885e4db1-a131-4727-80ab-3be8c591b766
title: FveEnableRawAccessW function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FveEnableRawAccessW
api_type: 
- DllExport
api_location: 
- Fveapi.dll
---

# FveEnableRawAccessW function

Enables or disables reading and writing of disk sectors.

## Syntax


```C++
HRESULT FveEnableRawAccessW(
  _In_ PCWSTR VolumeName,
  _In_ BOOL   Enabled
);
```



## Parameters

<dl> <dt>

*VolumeName* \[in\]
</dt> <dd>

A unique identifier for the disk volume.

</dd> <dt>

*Enabled* \[in\]
</dt> <dd>

If **TRUE**, allows access to the raw volume. If **FALSE**, no access is allowed to the raw volume. If raw access has already been enabled but this value is **FALSE**, the volume is remounted and revalidated.

</dd> </dl>

## Return value

This function returns one of the following codes or another error code if it fails.



| Return code/value                                                                                                                                                           | Description                                                                        |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl>                           | The function was successful.<br/>                                            |
| <dl> <dt>**S\_FALSE**</dt> <dt>1 (0x1)</dt> </dl>                        | Enabled is **FALSE** and the volume was not already in raw access mode.<br/> |
| <dl> <dt>**E\_ACCESSDENIED**</dt> <dt>2147942405 (0x80070005)</dt> </dl> | The volume cannot be locked.<br/>                                            |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| DLL<br/>                      | <dl> <dt>Fveapi.dll</dt> </dl> |



 

 




