---
title: StorPortAcquireSpinLock routine
description: The StorPortAcquireSpinLock routine acquires the specified spin lock.
ms.assetid: 52a877c7-b274-4bec-b948-edb0585a09e1
keywords:
- StorPortAcquireSpinLock routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortAcquireSpinLock
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

# StorPortAcquireSpinLock routine

The **StorPortAcquireSpinLock** routine acquires the specified spin lock.

## Syntax


```C++
VOID StorPortAcquireSpinLock(
  _In_    PVOID             DeviceExtension,
  _In_    STOR_SPINLOCK     SpinLock,
  _In_    PVOID             LockContext,
  _Inout_ PSTOR_LOCK_HANDLE LockHandle
);
```



## Parameters

<dl> <dt>

*DeviceExtension* \[in\]
</dt> <dd>

A pointer to the miniport driver per-adapter device extension.

</dd> <dt>

*SpinLock* \[in\]
</dt> <dd>

Contains an enumerator value of type [**STOR\_SPINLOCK**](stor-spinlock.md) that specifies the spin lock to acquire.

</dd> <dt>

*LockContext* \[in\]
</dt> <dd>

A pointer to the DPC object for which the lock is held if *SpinLock* indicates a type of **DpcLock**. This member should be **NULL** if *SpinLock* indicates a type of either **InterruptLock** or **StartIoLock**.

</dd> <dt>

*LockHandle* \[in, out\]
</dt> <dd>

A pointer to a buffer that, on return, will contain a lock handle. To release the lock, the caller must pass this handle to the [**StorPortReleaseSpinLock**](storportreleasespinlock.md) routine.

</dd> </dl>

## Return value

None

## Remarks

Miniport drivers must ensure that they do not attempt to acquire a lock that is already held or acquire locks in an incorrect order. Either of these mistakes will result in system deadlock.

Certain locks are held automatically by the port driver before it calls the miniport driver callback routines. For each miniport driver callback routine, the following table indicates which locks the port driver acquires automatically before calling the callback routine.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Miniport driver routine</th>
<th>Spin lock held by port driver</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>HwStorFindAdapter</strong>](hwstorfindadapter.md)<br/></td>
<td>None<br/></td>
</tr>
<tr class="even">
<td>[<strong>HwStorInitialize</strong>](hwstorinitialize.md)<br/></td>
<td>Interrupt (physical miniports), None (virtual miniports)<br/></td>
</tr>
<tr class="odd">
<td>[<strong>HwStorInterrupt</strong>](hwstorinterrupt.md)<br/></td>
<td>Interrupt<br/></td>
</tr>
<tr class="even">
<td>[<strong>HwMSIInterruptRoutine</strong>](hwmsinterruptroutine.md)<br/></td>
<td>Interrupt<br/></td>
</tr>
<tr class="odd">
<td>[<strong>HwStorStartIo</strong>](hwstorstartio.md)<br/></td>
<td>StartIo (physical miniports only when requested concurrent channels &lt;= 1)<br/></td>
</tr>
<tr class="even">
<td>[<strong>HwStorBuildIo</strong>](hwstorbuildio.md)<br/></td>
<td>None<br/></td>
</tr>
<tr class="odd">
<td>[<strong>HwStorTimer</strong>](hwstortimer.md)<br/></td>
<td>Startio, Interrupt (when <strong>SynchronizationModel</strong> member of [<strong>PORT_CONFIGURATION_INFORMATION</strong>](port-configuration-information--storport-.md) is set to <strong>StorSynchronizeHalfDuplex</strong>)<br/></td>
</tr>
<tr class="even">
<td>[<strong>HwStorResetBus</strong>](hwstorresetbus.md)<br/></td>
<td>Startio, Interrupt (when <strong>SynchronizationModel</strong> member of [<strong>PORT_CONFIGURATION_INFORMATION</strong>](port-configuration-information--storport-.md) is set to <strong>StorSynchronizeHalfDuplex</strong>)<br/></td>
</tr>
<tr class="odd">
<td>[<strong>HwStorAdapterControl</strong>](hwstoradaptercontrol.md)<br/></td>
<td>None<br/>
<blockquote>
[!Note]<br />
In Windows Server 2003, the StartIo spin lock was held when control type is ScsiStopAdapter.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>HwStorUnitControl</strong>](hwstorunitcontrol.md)<br/></td>
<td>None<br/></td>
</tr>
<tr class="odd">
<td>[<strong>HwStorTracingEnabled</strong>](hwstortracingenabled.md)<br/></td>
<td>None<br/></td>
</tr>
<tr class="even">
<td>[<strong>HwStorPassiveInitializeRoutine</strong>](hwstorpassiveinitializeroutine.md)<br/></td>
<td>None<br/></td>
</tr>
<tr class="odd">
<td>[<strong>HwStorDpcRoutine</strong>](hwstordpcroutine.md)<br/></td>
<td>None<br/></td>
</tr>
<tr class="even">
<td>[<strong>HwStorStateChange</strong>](hwstordpcroutine.md)<br/></td>
<td>Startio, Interrupt (when <strong>SynchronizationModel</strong> member of [<strong>PORT_CONFIGURATION_INFORMATION</strong>](port-configuration-information--storport-.md) is set to <strong>StorSynchronizeHalfDuplex</strong>)<br/></td>
</tr>
</tbody>
</table>



 

The locks held by the port driver influence which locks the callback routines are allowed to acquire, because spin locks must be acquired in the following order:

-   DPC or StartIo

-   Interrupt

For instance, if the port driver acquires the *Interrupt* spin lock before calling a callback routine, that callback routine can no longer acquire the *DPC* or *StartIo* spin lock because the *DPC* and *StartIo* spin locks are of a lower order than the *Interrupt* spin lock. On the other hand, if the port driver acquires the *StartIo* spin lock before calling a callback routine, that callback routine, when executed, could still acquire an *Interrupt* or a *DPC* spin lock.

The following table indicates which spin locks each miniport driver routine can acquire. In those cases where the miniport driver routine must obtain both the *StartIo* spin lock and the *Interrupt* spin lock, the routine must always acquire the *StartIo* spin lock first.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Miniport driver routine</th>
<th>Allowed spin locks</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>HwStorFindAdapter</strong>](hwstorfindadapter.md)<br/></td>
<td>None<br/></td>
</tr>
<tr class="even">
<td>[<strong>HwStorInitialize</strong>](hwstorinitialize.md)<br/></td>
<td>None<br/></td>
</tr>
<tr class="odd">
<td>[<strong>HwStorInterrupt</strong>](hwstorinterrupt.md)<br/></td>
<td>None<br/></td>
</tr>
<tr class="even">
<td>[<strong>HwMSIInterruptRoutine</strong>](hwmsinterruptroutine.md)<br/></td>
<td>None<br/></td>
</tr>
<tr class="odd">
<td>[<strong>HwStorStartIo</strong>](hwstorstartio.md)<br/></td>
<td>DPC, Interrupt<br/>
<blockquote>
[!Note]<br />
StartIo can be acquired in a virtual miniport driver or from a physical miniport driver that uses multiple concurrent channels.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>HwStorBuildIo</strong>](hwstorbuildio.md)<br/></td>
<td>DPC, StartIo, Interrupt<br/></td>
</tr>
<tr class="odd">
<td>[<strong>HwStorTimer</strong>](hwstortimer.md)<br/></td>
<td>Interrupt (when <strong>SynchronizationModel</strong> member of [<strong>PORT_CONFIGURATION_INFORMATION</strong>](port-configuration-information--storport-.md) is not set to <strong>StorSynchronizeHalfDuplex</strong>)<br/></td>
</tr>
<tr class="even">
<td>[<strong>HwStorResetBus</strong>](hwstorresetbus.md)<br/></td>
<td>Interrupt (when <strong>SynchronizationModel</strong> member of [<strong>PORT_CONFIGURATION_INFORMATION</strong>](port-configuration-information--storport-.md) is not set to <strong>StorSynchronizeHalfDuplex</strong>)<br/></td>
</tr>
<tr class="odd">
<td>[<strong>HwStorAdapterControl</strong>](hwstoradaptercontrol.md)<br/></td>
<td>DPC, StartIo, Interrupt<br/>
<blockquote>
[!Note]<br />
In Windows Server 2003, the no spin lock is allowed when control type is ScsiStopAdapter.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>HwStorUnitControl</strong>](hwstorunitcontrol.md)<br/></td>
<td>DPC, StartIo, Interrupt<br/></td>
</tr>
<tr class="odd">
<td>[<strong>HwStorTracingEnabled</strong>](hwstortracingenabled.md)<br/></td>
<td>DPC, StartIo, Interrupt<br/></td>
</tr>
<tr class="even">
<td>[<strong>HwStorPassiveInitializeRoutine</strong>](hwstorpassiveinitializeroutine.md)<br/></td>
<td>None<br/></td>
</tr>
<tr class="odd">
<td>[<strong>HwStorDpcRoutine</strong>](hwstordpcroutine.md)<br/></td>
<td>DPC, StartIo, Interrupt<br/></td>
</tr>
<tr class="even">
<td>[<strong>HwStorStateChange</strong>](hwstordpcroutine.md)<br/></td>
<td>Interrupt (when <strong>SynchronizationModel</strong> member of [<strong>PORT_CONFIGURATION_INFORMATION</strong>](port-configuration-information--storport-.md) is not set to <strong>StorSynchronizeHalfDuplex</strong>)<br/></td>
</tr>
</tbody>
</table>



 

## Requirements



|                                 |                                                                                                                                                                                     |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/>      | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl>                                             |
| Header<br/>               | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                                                                          |
| DDI compliance rules<br/> | [**StorPortSpinLock**](https://msdn.microsoft.com/library/windows/hardware/hh454273), [**StorPortSpinLock3**](https://msdn.microsoft.com/library/windows/hardware/hh454271), [**StorPortSpinLock4**](https://msdn.microsoft.com/library/windows/hardware/hh454272) |



## See also

<dl> <dt>

[**STOR\_SPINLOCK**](stor-spinlock.md)
</dt> <dt>

[**StorPortReleaseSpinLock**](storportreleasespinlock.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortAcquireSpinLock%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






