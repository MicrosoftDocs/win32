---
title: INTERRUPT\_SYNCHRONIZATION\_MODE enumeration
description: The INTERRUPT\_SYNCHRONIZATION\_MODE enumerator specifies the interrupt synchronization mode.
ms.assetid: '964009ab-5f90-4f23-b22a-4c3e03d2449e'
keywords: ["INTERRUPT_SYNCHRONIZATION_MODE enumeration Storage Devices"]
topic_type:
- apiref
api_name:
- INTERRUPT_SYNCHRONIZATION_MODE
api_location:
- storport.h
api_type:
- HeaderDef
---

# INTERRUPT\_SYNCHRONIZATION\_MODE enumeration

The INTERRUPT\_SYNCHRONIZATION\_MODE enumerator specifies the interrupt synchronization mode.

## Syntax


```C++
typedef enum _INTERRUPT_SYNCHRONIZATION_MODE { 
  InterruptSupportNone            = 0,
  InterruptSynchronizeAll         = 1,
  InterruptSynchronizePerMessage  = 2
} INTERRUPT_SYNCHRONIZATION_MODE;
```



## Constants

<dl> <dt>

<span id="InterruptSupportNone"></span><span id="interruptsupportnone"></span><span id="INTERRUPTSUPPORTNONE"></span>**InterruptSupportNone**
</dt> <dd>

MSI interrupts are not supported.

</dd> <dt>

<span id="InterruptSynchronizeAll"></span><span id="interruptsynchronizeall"></span><span id="INTERRUPTSYNCHRONIZEALL"></span>**InterruptSynchronizeAll**
</dt> <dd>

The Storport driver serializes all message signaled interrupts using a single interrupt spin lock. When an interrupt occurs, the Storport driver calls the miniport driver's [HwMSInterruptRoutine](hwmsinterruptroutine.md) routine at DIRQL after acquiring the interrupt spin lock.

</dd> <dt>

<span id="InterruptSynchronizePerMessage"></span><span id="interruptsynchronizepermessage"></span><span id="INTERRUPTSYNCHRONIZEPERMESSAGE"></span>**InterruptSynchronizePerMessage**
</dt> <dd>

The miniport driver serializes message signaled interrupts on a per message basis. In the synchronization per message mode, the Storport driver calls the miniport driver's [HwMSInterruptRoutine](hwmsinterruptroutine.md) routine at DIRQL holding the interrupt spin lock of the corresponding message. For more on the behavior of this synchronization mode, see the remarks section for HwMSInterruptRoutine.

</dd> </dl>

## Remarks

Miniport drivers define the HBA's interrupt synchronization mode by assigning one of the INTERRUPT\_SYNCHRONIZATION\_MODE enumeration values to the **InterruptSynchronizationMode** member of the [**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--storport-.md) structure.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Storport.h (include Storport.h)</dt> </dl> |



## See also

<dl> <dt>

[HwMSInterruptRoutine](hwmsinterruptroutine.md)
</dt> <dt>

[**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--storport-.md)
</dt> <dt>

[**StorPortAcquireMSISpinLock**](storportacquiremsispinlock.md)
</dt> <dt>

[**StorPortReleaseMSISpinLock**](storportreleasemsispinlock.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20INTERRUPT_SYNCHRONIZATION_MODE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






