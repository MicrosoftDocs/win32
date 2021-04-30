---
description: The SPFILENOTIFY\_FILEINCABINET notification is sent to a callback routine by SetupIterateCabinet for each file found in the cabinet. The callback routine must return a value indicating whether to extract the file.
ms.assetid: c6d89759-c0d4-4741-b992-43eaa0dc4f01
title: SPFILENOTIFY_FILEINCABINET message (Setupapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# SPFILENOTIFY\_FILEINCABINET message

The **SPFILENOTIFY\_FILEINCABINET** notification is sent to a callback routine by [**SetupIterateCabinet**](/windows/desktop/api/Setupapi/nf-setupapi-setupiteratecabineta) for each file found in the cabinet. The callback routine must return a value indicating whether to extract the file.


```C++
SPFILENOTIFY_FILEINCABINET
  Param1 = (UINT) FileInCabinetInfo;
  Param2 = (UINT) CabinetFile;
            
```



## Parameters

<dl> <dt>

*Param1* 
</dt> <dd>

Pointer to a [**FILE\_IN\_CABINET\_INFO**](/windows/desktop/api/Setupapi/ns-setupapi-file_in_cabinet_info_a) structure that contains information about the file in the cabinet.

</dd> <dt>

*Param2* 
</dt> <dd>

Pointer to a null-terminated string that contains the filename of the cabinet file.

</dd> </dl>

## Return value

Your callback routine should return one of the following.



| Return code                                                                                 | Description                                  |
|---------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>**FILEOP\_SKIP**</dt> </dl> | Do not extract the file, skip it.<br/> |
| <dl> <dt>**FILEOP\_DOIT**</dt> </dl> | Extract the file.<br/>                 |



 

If your callback routine returns FILEOP\_DOIT, the name to use for the extracted file should be specified in the **FullTargetName** member of the [**FILE\_IN\_CABINET\_INFO**](/windows/desktop/api/Setupapi/ns-setupapi-file_in_cabinet_info_a) structure passed to the routine in *Param1*.

> [!Note]  
> There is no default cabinet callback routine. The setup application should supply a callback routine to handle the notifications sent by [**SetupIterateCabinet**](/windows/desktop/api/Setupapi/nf-setupapi-setupiteratecabineta).

 

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

[**FILE\_IN\_CABINET\_INFO**](/windows/desktop/api/Setupapi/ns-setupapi-file_in_cabinet_info_a)
</dt> <dt>

[**SetupIterateCabinet**](/windows/desktop/api/Setupapi/nf-setupapi-setupiteratecabineta)
</dt> </dl>

 

 




