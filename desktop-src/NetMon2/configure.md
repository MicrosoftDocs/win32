---
description: Configures the expert within the expert DLL.
ms.assetid: 3906569d-9ad4-4c03-9637-f4a57697b227
title: Configure callback function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Configure
api_type: 
- UserDefined
api_location: 
- Netmon.h
---

# Configure callback function

The **Configure** function configures the expert within the expert DLL.

The expert must implement the **Configure** function. When the function call is received, the expert displays a dialog box that enables the user to change any configurable item.

## Syntax


```C++
BOOL WINAPI Configure(
  _In_    HEXPERTKEY         hExpertKey,
  _Inout_ PEXPERTCONFIG      *ppConfig,
  _In_    PEXPERTSTARTUPINFO pExpertStartupInfo,
  _In_    DWORD              StartupFlags,
  _In_    HWND               hWnd
);
```



## Parameters

<dl> <dt>

*hExpertKey* \[in\]
</dt> <dd>

Unique expert identifier.

The unique identifier is passed back on all expert-specific Network Monitor functions. Be aware that the identifier may not be the same expert key as the one passed to the [**Run**](run.md) function. Do not store the expert key from the **Configure** call.

</dd> <dt>

*ppConfig* \[in, out\]
</dt> <dd>

A pointer to a pointer to an [**EXPERTCONFIG**](expertconfig.md) structure upon entry.

After a successful exit, the referenced [**EXPERTCONFIG**](expertconfig.md) structure contains the new configuration data.

</dd> <dt>

*pExpertStartupInfo* \[in\]
</dt> <dd>

A pointer to the capture element with focus when the expert started.

</dd> <dt>

*StartupFlags* \[in\]
</dt> <dd>

The flags that indicate how the expert should use the *pExpertStartupInfo* parameter. The only flag defined is **EXPERT\_STARTUP\_FLAG\_USE\_STARTUP\_DATA\_OVER\_CONFIG\_DATA**. The flag indicates that the expert will use the *pExpertStartupInfo* parameter rather than the *ppConfig* parameter that passed in. Typically, you set the flag when you start the expert from a context menu.

</dd> <dt>

*hWnd* \[in\]
</dt> <dd>

A handle to the parent window. Use the handle to open a dialog box.

</dd> </dl>

## Return value

If the function is successful (that is, if a current configuration exists), the return value is **TRUE**.

If the function is unsuccessful, the return value is **FALSE**.

## Remarks

Network Monitor calls the **Configure** function with the current configuration of the expert, if one exists. The expert displays a dialog box, with which you can change any configurable item.

When *ppConfig* is passed in and Network Monitor does not have a configuration stored for the specified expert, the parameter value can be **NULL**. In this case, the **Configure** function assumes hard-coded default values (or, uses the startup information) to open the dialog box.

The configuration data can also be **NULL** when the **Configure** function returns, and a **NULL** was passed-in. This situation occurs when Network Monitor does not have a stored default, and the user presses **Cancel**.

The beginning of the [**EXPERTCONFIG**](expertconfig.md) data structure includes a Private section that stores the structure size information. The size of the **EXPERTCONFIG** structure should include the reserved **DWORD** length that appears at the beginning of the structure. For example, if your configuration data requires 20 bytes of storage space, allocate 24 bytes to store the data. If a *ppConfig* is **NULL**, the **Configure** function calls the [**ExpertAllocMemory**](expertallocmemory.md) function to allocate a new configuration that is the correct size. If the buffer is not enough to hold the expert data, the expert should call the [**ExpertReallocMemory**](expertreallocmemory.md) function.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




