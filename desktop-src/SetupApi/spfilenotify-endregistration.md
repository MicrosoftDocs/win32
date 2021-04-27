---
description: SPFILENOTIFY_ENDREGISTRATION message - When using the RegisterDlls INF directive to self-register DLLs, callers of SetupInstallFromInfSection may receive notifications on each file as it is registered or unregistered.
ms.assetid: 6304f406-c9f8-41cc-a7b7-5ef606f62efb
title: SPFILENOTIFY_ENDREGISTRATION message (Setupapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# SPFILENOTIFY\_ENDREGISTRATION message

When using the **RegisterDlls** INF directive to self-register DLLs, callers of [**SetupInstallFromInfSection**](/windows/desktop/api/Setupapi/nf-setupapi-setupinstallfrominfsectiona) may receive notifications on each file as it is registered or unregistered. To send a **SPFILENOTIFY\_ENDREGISTRATION** notification to a callback routine once after registering or unregistering a file, include SPINST\_REGISTERCALLBACKAWARE plus SPINST\_REGSVR in the *Flags* parameter of **SetupInstallFromInfSection**. To send notification of unregistration, include SPINST\_REGISTERCALLBACKAWARE plus SPINST\_UNREGSVR in the *Flags* parameter.

The callback routine specified by the *MsgHandler* parameter of [**SetupInstallFromInfSection**](/windows/desktop/api/Setupapi/nf-setupapi-setupinstallfrominfsectiona) must be the type [PSP\_FILE\_CALLBACK](/windows/win32/api/setupapi/nc-setupapi-psp_file_callback_a). Set the *Context* parameter to the same *Context* specified in **SetupInstallFromInfSection**. Set the *Notification* parameter to **SPFILENOTIFY\_ENDREGISTRATION**.


```C++
SPFILENOTIFY_ENDREGISTRATION
  Param1 = (UINT_PTR) pointer to file information;
  Param2 = (UINT_PTR) file registration or unregistration;
            
```



## Parameters

<dl> <dt>

*Param1* 
</dt> <dd>

Pointer to a [**SP\_REGISTER\_CONTROL\_STATUS**](/windows/desktop/api/Setupapi/ns-setupapi-sp_register_control_statusa) structure containing information about the file being registered or unregistered. The member **cbsize** should be set to the size of the structure. **FileName** should be set to the fully qualified path of the file being registered. **Win32Error** should be set to a [system error code](/windows/desktop/Debug/system-error-codes) indicating an extended error code. **FailureCode** should be set to one of the valid failure codes indicating the outcome of the registration. For valid failure codes see [**SP\_REGISTER\_CONTROL\_STATUS**](/windows/desktop/api/Setupapi/ns-setupapi-sp_register_control_statusa).

</dd> <dt>

*Param2* 
</dt> <dd>

If the file is being registered, *Param2* should be set to a pointer to a nonzero value. If the file is being unregistered, *Param2* should be set to a pointer to zero.

</dd> </dl>

## Return value

After receiving notification, the callback function may return one of the following values.



| Return code                                                                                  | Description                                     |
|----------------------------------------------------------------------------------------------|-------------------------------------------------|
| <dl> <dt>**FILEOP\_ABORT**</dt> </dl> | Stop processing the INF section.<br/>     |
| <dl> <dt>**FILEOP\_DOIT**</dt> </dl>  | Continue processing the INF section.<br/> |
| <dl> <dt>**FILE\_SKIP**</dt> </dl>    | Continue processing the INF section<br/>  |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Setupapi.h</dt> </dl> |



## See also

<dl> <dt>

[Overview](overview.md)
</dt> <dt>

[Notifications](notifications.md)
</dt> <dt>

[**SetupInstallFromInfSection**](/windows/desktop/api/Setupapi/nf-setupapi-setupinstallfrominfsectiona)
</dt> <dt>

[**SPFILENOTIFY\_STARTREGISTRATION**](spfilenotify-startregistration.md)
</dt> </dl>

 

