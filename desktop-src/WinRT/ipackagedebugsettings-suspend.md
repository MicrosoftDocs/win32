---
description: Suspends the processes of the package if they are currently running.
ms.assetid: 83f44285-46ed-4968-b0af-7964dfacf602
title: IPackageDebugSettings::Suspend method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPackageDebugSettings.Suspend
api_type: 
- COM
api_location: 
- Shobjidl.idl
---

# IPackageDebugSettings::Suspend method

Suspends the processes of the package if they are currently running.

## Syntax


```C++
HRESULT Suspend(
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

This method can return one of these values.



| Return code                                                                                            | Description                                      |
|--------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                   | The operation succeeded.<br/>              |
| <dl> <dt>**E\_ILLEGAL\_STATECHANGE**</dt> </dl> | The process is not currently running.<br/> |



 

## Remarks

Each process receives the [**Suspending**](/uwp/api/Windows.ApplicationModel.Core.CoreApplication?view=winrt-19041) event. It can be useful for developers to step through how their apps respond to this event.

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

 

 
