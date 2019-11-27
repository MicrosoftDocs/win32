---
Description: The UnregisterTraceGuids function unregisters an event trace provider and its event trace classes.
ms.assetid: 1fa10f66-a78b-4f40-9518-72d48365246e
title: UnregisterTraceGuids function (Evntrace.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- UnregisterTraceGuids
api_type: 
- DllExport
api_location: 
- Advapi32.dll
- API-MS-Win-DownLevel-AdvApi32-l1-1-0.dll
- KernelBase.dll
- API-MS-Win-DownLevel-AdvApi32-l1-1-1.dll
- API-MS-Win-eventing-classicprovider-l1-1-0.dll
---

# UnregisterTraceGuids function

The **UnregisterTraceGuids** function unregisters an event trace provider and its event trace classes.

## Syntax


```C++
ULONG UnregisterTraceGuids(
  _In_ TRACEHANDLE RegistrationHandle
);
```



## Parameters

<dl> <dt>

*RegistrationHandle* \[in\]
</dt> <dd>

Handle to the event trace provider, obtained from an earlier call to the [**RegisterTraceGuids**](registertraceguids.md) function.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value is one of the [system error codes](https://msdn.microsoft.com/library/ms681381(v=VS.85).aspx). The following table includes some common errors and their causes.



| Return code                                                                                              | Description                                                                                                         |
|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**ERROR\_INVALID\_PARAMETER**</dt> </dl> | The *RegistrationHandle* parameter does not specify the handle to a registered provider or is **NULL**. <br/> |



 

## Remarks

Providers call this function.

The event trace provider must have been registered previously by calling the [**RegisterTraceGuids**](registertraceguids.md) function.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps \| UWP apps\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps \| UWP apps\]<br/>                             |
| Minimum supported phone<br/>  | Windows Phone 8.1<br/>                                                            |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Advapi32.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Advapi32.dll</dt> </dl> |



## See also

<dl> <dt>

[**RegisterTraceGuids**](registertraceguids.md)
</dt> </dl>

 

 




