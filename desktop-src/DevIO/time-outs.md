---
Description: A handle to a communications resource has an associated set of time-out parameters that affect the behavior of read and write operations.
ms.assetid: 271d4c68-1f6d-4483-a9a1-703220de761f
title: Time-Outs
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Time-Outs

A handle to a communications resource has an associated set of time-out parameters that affect the behavior of read and write operations. Time-outs can cause a [**ReadFile**](https://msdn.microsoft.com/library/windows/desktop/aa365467), [**ReadFileEx**](https://msdn.microsoft.com/library/windows/desktop/aa365468), [**WriteFile**](https://msdn.microsoft.com/library/windows/desktop/aa365747), or [**WriteFileEx**](https://msdn.microsoft.com/library/windows/desktop/aa365748) operation to conclude when a time-out interval elapses, even though the specified number of characters have not been read or written. It is not treated as an error when a time-out occurs during a read or write operation (that is, the read or write function's return value indicates success). The count of bytes actually read or written is reported by **ReadFile** or **WriteFile** (or by the [**GetOverlappedResult**](https://msdn.microsoft.com/library/windows/desktop/ms683209) or [**FileIOCompletionRoutine**](https://msdn.microsoft.com/library/windows/desktop/aa364052) function, if the I/O was performed as an overlapped operation).

When an application opens a communications resource, the system sets the resource's time-out values to the values in effect when the resource was last used. If the communications resource has never been opened, the system sets the time-out values to some default value. In either case, an application should always determine the current time-out values after opening the resource, and then explicitly set them to meet its requirements. To determine the current time-out values of a communications resource, use the [**GetCommTimeouts**](/windows/win32/Winbase/nf-winbase-getcommtimeouts?branch=master) function. To change the time-out values, use the [**SetCommTimeouts**](/windows/win32/Winbase/nf-winbase-setcommtimeouts?branch=master) function.

Two types of time-outs are enabled by the time-out parameters. An interval time-out occurs when the time between the receipt of any two characters exceeds a specified number of milliseconds. Timing starts when the first character is received and is restarted when each new character is received. A total time-out occurs when the total amount of time consumed by a read operation exceeds a calculated number of milliseconds. Timing starts immediately when the I/O operation begins. Write operations support only total time-outs. Read operations support both interval and total time-outs, which can be used separately or combined.

The time, in milliseconds, of the total time-out period for a read or write operation is calculated by using the multiplier and constant values from the [**COMMTIMEOUTS**](/windows/win32/Winbase/ns-winbase-_commtimeouts?branch=master) structure specified in the [**GetCommTimeouts**](/windows/win32/Winbase/nf-winbase-getcommtimeouts?branch=master) or [**SetCommTimeouts**](/windows/win32/Winbase/nf-winbase-setcommtimeouts?branch=master) function. The following formula is used:


```C++
Timeout = (MULTIPLIER * number_of_bytes) + CONSTANT
```



Using both a multiplier and a constant enables the total time-out period to vary, depending on the amount of data being requested. An application can use only the constant by setting the multiplier to zero, or use only the multiplier by setting the constant to zero. If both the constant and multiplier are zero, total time-out is not used.

If all read time-out parameters are zero, read time-outs are not used, and a read operation is not complete until the requested number of bytes have been read or an error occurs. Similarly, if all write time-out parameters are zero, a write operation is not completed until the requested number of bytes have been written or an error occurs.

If the read interval time-out parameter is the **MAXDWORD** value and both read total time-out parameters are zero, a read operation is completed immediately after reading whatever characters are available in the input buffer, even if it is empty.

Interval timing forces a read operation to return when there is a lull in reception. A process using interval time-outs can set a fairly short interval parameter, so it can respond quickly to small, isolated bursts of one or a few characters, yet it can still collect large buffers of characters with a single call when data is received in a steady stream.

Time-outs for a write operation can be useful when transmission is blocked by some kind of flow control or when the [**SetCommBreak**](/windows/win32/Winbase/nf-winbase-setcommbreak?branch=master) function has been called to suspend character transmission.

The following table summarizes the behavior of read operations based on the values specified for total and interval time-outs.



| Total | Interval | Behavior                                                                                                                                                                                 |
|-------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0     | 0        | Returns when the buffer is completely filled. Time-outs are not used.                                                                                                                    |
| T     | 0        | Returns when the buffer is completely filled or when T milliseconds have elapsed since the beginning of the operation.                                                                   |
| 0     | Y        | Returns when the buffer is completely filled or when Y milliseconds have elapsed between the receipt of any two characters. Timing does not begin until the first character is received. |
| T     | Y        | Returns when the buffer is completely filled or when either type of time-out occurs.                                                                                                     |



 

> [!Note]  
> However, that timing is relative to the system controlling the physical device. For a remote device such as a modem, the timing is relative to the server system to which the modem is attached. Any network propagation delay is not factored in. For example, a client application might specify a total time-out that computes to be 500 milliseconds. When 500 milliseconds have elapsed at the server, a time-out error is returned to the client. If there is a 50 milliseconds network propagation delay, the client will not be notified of the time-out until approximately 50 milliseconds after the time-out actually occurred.

 

> [!Note]  
> The time-out parameters affect the behavior of overlapped read and write operations on a communications device. With overlapped I/O, the [**ReadFile**](https://msdn.microsoft.com/library/windows/desktop/aa365467), [**WriteFile**](https://msdn.microsoft.com/library/windows/desktop/aa365747), [**ReadFileEx**](https://msdn.microsoft.com/library/windows/desktop/aa365468), or [**WriteFileEx**](https://msdn.microsoft.com/library/windows/desktop/aa365748) function can return before the operation has been completed. The time-out parameters can determine when the operation has been completed.

 

 

 



