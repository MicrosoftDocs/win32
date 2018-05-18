---
Description: MPI Point to Point Functions
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '59F2FC56-63FF-4F3B-895A-9639AD57415D'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: MPI Point to Point Functions
---

# MPI Point to Point Functions

## In this section

<dl> <dt>

[**MPI\_Bsend**](mpi-bsend.md)
</dt> <dd>

Sends data to a specified process in buffered mode.

</dd> <dt>

[**MPI\_Bsend\_init**](mpi-bsend-init.md)
</dt> <dd>

TBD

</dd> <dt>

[**MPI\_Cancel**](mpi-cancel.md)
</dt> <dd>

TBD

</dd> <dt>

[**MPI\_Get\_count**](mpi-get-count.md)
</dt> <dd>

TBD

</dd> <dt>

[**MPI\_Ibsend**](mpi-ibsend.md)
</dt> <dd>

Initiates a buffered mode send operation and returns a handle to the communication operation.

</dd> <dt>

[**MPI\_Iprobe**](mpi-iprobe.md)
</dt> <dd>

TBD

</dd> <dt>

[**MPI\_Improbe**](mpi-improbe.md)
</dt> <dd>

Probes for a message in a non-blocking way. Provides a mechanism to receive the specific message that was matched regardless of intervening probe/receive operations. The matched message is de-queued off the receive queue, giving the application an opportunity to decide how to receive the message based on the information returned by the non-blocking matching probe operation. The matched message is then received using the [**MPI\_Mrecv**](mpi-mrecv.md) or [**MPI\_Imrecv**](mpi-imrecv.md) function.

</dd> <dt>

[**MPI\_Imrecv**](mpi-imrecv.md)
</dt> <dd>

Performs a non-blocking receive for a message matched by [**MPI\_Mprobe**](mpi-mprobe.md) or [**MPI\_Improbe**](mpi-improbe.md).

</dd> <dt>

[**MPI\_Irecv**](mpi-irecv.md)
</dt> <dd>

Initiates a receive operation and returns a handle to the requested communication operation.

</dd> <dt>

[**MPI\_Irsend**](mpi-irsend.md)
</dt> <dd>

Initiates a ready mode send operation and returns a request handle that represents the communication operation.

</dd> <dt>

[**MPI\_Isend**](mpi-isend.md)
</dt> <dd>

Initiates a standard mode send operation and returns a handle to the requested communication operation.

</dd> <dt>

[**MPI\_Issend**](mpi-issend.md)
</dt> <dd>

Initiates a synchronous mode send operation and returns a handle to the requested communication operation.

</dd> <dt>

[**MPI\_Mprobe**](mpi-mprobe.md)
</dt> <dd>

Blocking probes for a message. Provides a mechanism to receive the specific message that was matched regardless of intervening probe/receive operations. The matched message is de-queued off the receive queue, giving the application an opportunity to decide how to receive the message based on the information returned by the matching probe operation. The matched message is then received using the [**MPI\_Mrecv**](mpi-mrecv.md) or [**MPI\_Imrecv**](mpi-imrecv.md) function.

</dd> <dt>

[**MPI\_Mrecv**](mpi-mrecv.md)
</dt> <dd>

Performs a blocking receive for a message matched by [**MPI\_Mprobe**](mpi-mprobe.md) or [**MPI\_Improbe**](mpi-improbe.md).

</dd> <dt>

[**MPI\_Probe**](mpi-probe.md)
</dt> <dd>

TBD

</dd> <dt>

[**MPI\_Recv**](mpi-recv.md)
</dt> <dd>

Performs a receive operation and does not return until a matching message is received.

</dd> <dt>

[**MPI\_Recv\_init**](mpi-recv-init.md)
</dt> <dd>

TBD

</dd> <dt>

[**MPI\_Request\_free**](mpi-request-free.md)
</dt> <dd>

TBD

</dd> <dt>

[**MPI\_Request\_get\_status**](mpi-request-get-status.md)
</dt> <dd>

TBD

</dd> <dt>

[**MPI\_Rsend**](mpi-rsend.md)
</dt> <dd>

Performs a ready mode send operation and returns when the send buffer can be safely reused.

</dd> <dt>

[**MPI\_Rsend\_init**](mpi-rsend-init.md)
</dt> <dd>

TBD

</dd> <dt>

[**MPI\_Send**](mpi-send.md)
</dt> <dd>

Performs a standard mode send operation and returns when the send buffer can be safely reused.

</dd> <dt>

[**MPI\_Send\_init**](mpi-send-init.md)
</dt> <dd>

TBD

</dd> <dt>

[**MPI\_Sendrecv**](mpi-sendrecv.md)
</dt> <dd>

TBD

</dd> <dt>

[**MPI\_Sendrecv\_replace**](mpi-sendrecv-replace.md)
</dt> <dd>

TBD

</dd> <dt>

[**MPI\_Ssend**](mpi-ssend.md)
</dt> <dd>

Performs a synchronous mode send operation and returns when the send buffer can be safely reused.

</dd> <dt>

[**MPI\_Ssend\_init**](mpi-ssend-init.md)
</dt> <dd>

TBD

</dd> <dt>

[**MPI\_Start**](mpi-start.md)
</dt> <dd>

TBD

</dd> <dt>

[**MPI\_Startall**](mpi-startall.md)
</dt> <dd>

TBD

</dd> <dt>

[**MPI\_Test**](mpi-test.md)
</dt> <dd>

Tests an outstanding operation for completion.

</dd> <dt>

[**MPI\_Test\_cancelled**](mpi-test-cancelled.md)
</dt> <dd>

TBD

</dd> <dt>

[**MPI\_Testall**](mpi-testall.md)
</dt> <dd>

TBD

</dd> <dt>

[**MPI\_Testany**](mpi-testany.md)
</dt> <dd>

TBD

</dd> <dt>

[**MPI\_Testsome**](mpi-testsome.md)
</dt> <dd>

TBD

</dd> <dt>

[**MPI\_Wait**](mpi-wait.md)
</dt> <dd>

Completes an outstanding operation.

</dd> <dt>

[**MPI\_Waitall**](mpi-waitall.md)
</dt> <dd>

Completes multiple outstanding operations.

</dd> <dt>

[**MPI\_Waitany**](mpi-waitany.md)
</dt> <dd>

Completes one out of several outstanding operations.

</dd> <dt>

[**MPI\_Waitsome**](mpi-waitsome.md)
</dt> <dd>

TBD

</dd> <dt>

[**MSMPI\_Queuelock\_acquire**](msmpi-queuelock-acquire.md)
</dt> <dd>

Acquires the Microsoft MPI library global lock.

</dd> <dt>

[**MSMPI\_Queuelock\_release**](msmpi-queuelock-release.md)
</dt> <dd>

Releases the Microsoft MPI library global lock.

</dd> <dt>

[**MSMPI\_Waitsome\_interruptible**](msmpi-waitsome-interruptible.md)
</dt> <dd>

Waits until at least one of the operations that is associated with active handles in the list has finished, or the call is interrupted by another thread that calls [**MSMPI\_Queuelock\_acquire**](msmpi-queuelock-acquire.md).

</dd> </dl>

 

 



