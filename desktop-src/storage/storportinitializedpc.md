---
title: StorPortInitializeDpc routine
description: The StorPortInitializeDpc routine initializes a StorPort DPC.
ms.assetid: 0a67304f-c746-46c1-87c4-5d027219e41f
keywords:
- StorPortInitializeDpc routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortInitializeDpc
api_location:
- storport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# StorPortInitializeDpc routine

The **StorPortInitializeDpc** routine initializes a StorPort DPC.

## Syntax


```C++
VOID StorPortInitializeDpc(
  _In_  PVOID           DeviceExtension,
  _Out_ PSTOR_DPC       Dpc,
  _In_  PHW_DPC_ROUTINE HwDpcRoutine
);
```



## Parameters

<dl> <dt>

*DeviceExtension* \[in\]
</dt> <dd>

Pointer to the per-adapter device extension.

</dd> <dt>

*Dpc* \[out\]
</dt> <dd>

Pointer to a buffer where a DPC object of type [**STOR\_DPC**](stor-dpc.md) will be created. The caller must ensure that the size in bytes of this buffer is greater than or equal to **sizeof**(STOR\_DPC).

</dd> <dt>

*HwDpcRoutine* \[in\]
</dt> <dd>

Pointer to the DPC routine that corresponds to the DPC object pointed to by *Dpc*. The prototype for this deferred routine is defined in Storport.h as follows:


```
typedef
VOID
(*PHW_DPC_ROUTINE) 
  IN PSTOR_DPC  Dpc,
  IN PVOID  HwDeviceExtension,
  IN PVOID  SystemArgument1,
  IN PVOID  SystemArgument2
  );
```



</dd> </dl>

## Return value

None.

## Remarks

The **StorPortInitializeDpc** routine must be called during HBA initialization from within the miniport driver's [**HwStorPassiveInitializeRoutine**](hwstorpassiveinitializeroutine.md) routine.

This routine is implemented using inline function definitions, so that miniport drivers that use this routine will not have to link to libraries that are dependent on the version of the operating system. Miniport drivers can use this routine without sacrificing backward compatibility with versions of the operating system that do not support DPCs in storage miniport drivers.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |



## See also

<dl> <dt>

[**HwStorPassiveInitializeRoutine**](hwstorpassiveinitializeroutine.md)
</dt> <dt>

[**STOR\_DPC**](stor-dpc.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortInitializeDpc%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






