---
Description: The locally unique identifier (LUID) is a 64-bit value guaranteed to be unique only on the system on which it was generated.
ms.assetid: 564bcc9a-943b-4ad9-aeaa-0af4c3d3da0c
title: LUID
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LUID

The locally unique identifier (LUID) is a 64-bit value guaranteed to be unique only on the system on which it was generated. The uniqueness of an LUID is guaranteed only until the system is restarted.

An LUID is not for direct manipulation. Drivers must use support routines and structures to manipulate LUID values.

``` syntax
typedef struct _LUID {
  ULONG  LowPart;
  LONG  HighPart;
} LUID, *PLUID;
```

## Requirements



|                   |                                                                                                      |
|-------------------|------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdef.h (include Ntifs.h)</dt> </dl> |



## See also

<dl> <dt>

[**LUID\_AND\_ATTRIBUTES**](/windows-hardware/drivers/ddi/content/wdm/ns-wdm-_luid_and_attributes)
</dt> <dt>

[**RtlConvertLongToLuid**](https://msdn.microsoft.com/bc03feaf-ee98-4b47-a659-809b5b8b9364)
</dt> <dt>

[**RtlConvertUlongToLuid**](https://msdn.microsoft.com/f3c1e2d5-8bb8-486c-a78a-3ddde6ab64bd)
</dt> <dt>

[**RtlCopyLuid**](/windows-hardware/drivers/ddi/content/ntifs/nf-ntifs-rtlcopyluid)
</dt> <dt>

[**RtlEqualLuid**](https://www.bing.com/search?q=**RtlEqualLuid**)
</dt> <dt>

[**SeMarkLogonSessionForTerminationNotification**](/windows-hardware/drivers/ddi/content/ntifs/nf-ntifs-semarklogonsessionforterminationnotification)
</dt> <dt>

[**SeQueryAuthenticationIdToken**](/windows-hardware/drivers/ddi/content/ntifs/nf-ntifs-sequeryauthenticationidtoken)
</dt> <dt>

[**SeSinglePrivilegeCheck**](https://msdn.microsoft.com/bb83318c-b14f-421a-9cd4-69e270b825c7)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20LUID%20%20RELEASE:%20%283/30/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





