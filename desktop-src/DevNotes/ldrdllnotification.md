---
description: A notification callback function specified with the LdrRegisterDllNotification function.
ms.assetid: 12202797-c80c-4fa3-9cc4-dcb1a9f01551
title: LdrDllNotification callback function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LdrDllNotification
- PLDR_DLL_NOTIFICATION_FUNCTION
api_type: 
- UserDefined
api_location: 
---

# LdrDllNotification callback function

\[This function may be changed or removed from Windows without further notice.\]

A notification callback function specified with the [**LdrRegisterDllNotification**](ldrregisterdllnotification.md) function. The loader calls this function when a DLL is first loaded.

**Warning:** It is unsafe for the notification callback function to call functions in any DLL.

## Syntax


```C++
VOID CALLBACK LdrDllNotification(
  _In_     ULONG                       NotificationReason,
  _In_     PCLDR_DLL_NOTIFICATION_DATA NotificationData,
  _In_opt_ PVOID                       Context
);
```



## Parameters

<dl> <dt>

*NotificationReason* \[in\]
</dt> <dd>

The reason that the notification callback function was called. This parameter can be one of the following values.



| Value                                                                                                                                                                                                                                                                                        | Meaning                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <span id="LDR_DLL_NOTIFICATION_REASON_LOADED"></span><span id="ldr_dll_notification_reason_loaded"></span><dl> <dt>**LDR\_DLL\_NOTIFICATION\_REASON\_LOADED**</dt> <dt>1</dt> </dl>       | The DLL was loaded. The *NotificationData* parameter points to an **LDR\_DLL\_LOADED\_NOTIFICATION\_DATA** structure. <br/>     |
| <span id="LDR_DLL_NOTIFICATION_REASON_UNLOADED"></span><span id="ldr_dll_notification_reason_unloaded"></span><dl> <dt>**LDR\_DLL\_NOTIFICATION\_REASON\_UNLOADED**</dt> <dt>2</dt> </dl> | The DLL was unloaded. The *NotificationData* parameter points to an **LDR\_DLL\_UNLOADED\_NOTIFICATION\_DATA** structure. <br/> |



 

</dd> <dt>

*NotificationData* \[in\]
</dt> <dd>

A pointer to a constant **LDR\_DLL\_NOTIFICATION** union that contains notification data. This union has the following definition:

``` syntax
typedef union _LDR_DLL_NOTIFICATION_DATA {
    LDR_DLL_LOADED_NOTIFICATION_DATA Loaded;
    LDR_DLL_UNLOADED_NOTIFICATION_DATA Unloaded;
} LDR_DLL_NOTIFICATION_DATA, *PLDR_DLL_NOTIFICATION_DATA;
```

The **LDR\_DLL\_LOADED\_NOTIFICATION\_DATA** structure has the following definition:

``` syntax
typedef struct _LDR_DLL_LOADED_NOTIFICATION_DATA {
    ULONG Flags;                    //Reserved.
    PCUNICODE_STRING FullDllName;   //The full path name of the DLL module.
    PCUNICODE_STRING BaseDllName;   //The base file name of the DLL module.
    PVOID DllBase;                  //A pointer to the base address for the DLL in memory.
    ULONG SizeOfImage;              //The size of the DLL image, in bytes.
} LDR_DLL_LOADED_NOTIFICATION_DATA, *PLDR_DLL_LOADED_NOTIFICATION_DATA;
```

The **LDR\_DLL\_UNLOADED\_NOTIFICATION\_DATA** structure has the following definition:

``` syntax
typedef struct _LDR_DLL_UNLOADED_NOTIFICATION_DATA {
    ULONG Flags;                    //Reserved.
    PCUNICODE_STRING FullDllName;   //The full path name of the DLL module.
    PCUNICODE_STRING BaseDllName;   //The base file name of the DLL module.
    PVOID DllBase;                  //A pointer to the base address for the DLL in memory.
    ULONG SizeOfImage;              //The size of the DLL image, in bytes.
} LDR_DLL_UNLOADED_NOTIFICATION_DATA, *PLDR_DLL_UNLOADED_NOTIFICATION_DATA;
```

</dd> <dt>

*Context* \[in, optional\]
</dt> <dd>

A pointer to context data for the callback function.

</dd> </dl>

## Return value

This callback function does not return a value.

## Remarks

The notification callback function is called before dynamic linking takes place.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**LdrRegisterDllNotification**](ldrregisterdllnotification.md)
</dt> <dt>

[**LdrUnregisterDllNotification**](ldrunregisterdllnotification.md)
</dt> </dl>

 

 




