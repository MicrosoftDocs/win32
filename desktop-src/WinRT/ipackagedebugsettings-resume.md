---
description: Resumes the processes of the package if they are currently suspended.
ms.assetid: c5376e00-b4b7-4a81-a84c-3a46758fe130
title: IPackageDebugSettings::Resume method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPackageDebugSettings.Resume
api_type: 
- COM
api_location: 
- Shobjidl.idl
---

# IPackageDebugSettings::Resume method

Resumes the processes of the package if they are currently suspended.

## Syntax


```C++
HRESULT Resume(
  [in] LPCWSTR packageFullName
);
```



## Parameters

<dl> <dt>

*packageFullName* \[in\]
</dt> <dd>

Type: **LPCWSTR**

The package full name.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Each process receives the [**Resuming**](/uwp/api/Windows.ApplicationModel.Core.CoreApplication?view=winrt-19041) event. It can be useful for developers to step through how their apps respond to this event.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| IDL<br/>                      | <dl> <dt>Shobjidl.idl</dt> </dl> |



## See also

<dl> <dt>

[**IPackageDebugSettings**](/previous-versions//hh438393(v=vs.85))
</dt> </dl>

 

 
