---
description: Synchronizing DVD Commands
ms.assetid: 37e8f940-617d-43f6-92bd-aadccafe0059
title: Synchronizing DVD Commands
ms.topic: article
ms.date: 05/31/2018
---

# Synchronizing DVD Commands

DVD commands do not always complete instantly. For this reason, some of the methods in [**IDvdControl2**](/windows/desktop/api/Strmif/nn-strmif-idvdcontrol2) are asynchronous. These include playback methods, such as **PlayTitle**, and menu navigation methods, such as **ShowMenu** and **ReturnFromSubmenu**. An asynchronous method returns immediately, without waiting for the command to complete. After the method returns, other events may prevent the command from completing, even if the method succeeded. DirectShow provides several options for synchronizing commands, ranging from no synchronization to full synchronization using filter graph events.

All of the asynchronous methods have a *dwFlags* parameter and a *ppCmd* parameter. The *dwFlags* parameter specifies the synchronization behavior, and the *ppCmd* parameter returns a pointer to an optional synchronization object. Different behaviors result depending on what values you give for these parameters.

**No Synchronization**

For a basic DVD playback application, the best option may be simply to ignore synchronization issues. Occasionally a command may fail or the UI might lag slightly when it updates, but these errors will be on the order of fractions of seconds.

To issue a command with no synchronization, set the DVD\_CMD\_FLAG\_None flag in the *dwFlags* parameter and set the *ppCmd* parameter to **NULL**:


```C++
hr = pDVDControl2->PlayTitle(uTitle, DVD_CMD_FLAG_None, NULL);
```



**Blocking**

If you set the EC\_DVD\_CMD\_FLAG\_Block flag in the *dwFlags* parameter, the method blocks until the command completes:


```C++
hr = pDVDControl2->PlayTitle(uTitle, EC_DVD_CMD_FLAG_Block, NULL);
```



In effect, this flag turns an asynchronous method into a synchronous method. The drawback is that your UI blocks if you call the method from the application thread.

**Synchronization Object**

All of the asynchronous methods can return a synchronization object, which you can use to wait for the command to start or end. To get this object, pass the address of an [**IDvdCmd**](/windows/desktop/api/Strmif/nn-strmif-idvdcmd) pointer in the *ppCmd* parameter:


```C++
IDvdCmd *pCmdObj = NULL;
hr = pDVDControl2->PlayTitle(uTitle, DVD_CMD_FLAG_None, &pCmdObj);
```



If the method succeeds, it returns a new **IDvdCmd** object. The [**IDvdCmd::WaitForStart**](/windows/desktop/api/Strmif/nf-strmif-idvdcmd-waitforstart) method blocks until the command begins, and the [**IDvdCmd::WaitForEnd**](/windows/desktop/api/Strmif/nf-strmif-idvdcmd-waitforend) method blocks until the command ends. The return value indicates the status of the command.

The following code is functionally equivalent to setting the EC\_DVD\_CMD\_FLAG\_Block flag, shown previously.


```C++
IDvdCmd *pCmdObj = NULL;
hr = pDVDControl2->PlayTitle(uTitle, DVD_CMD_FLAG_None, &pCmdObj);
if (SUCCEEDED(hr))
{
    // Use pCmdObj to wait for the command to complete.
    hr = pCmdObj->WaitToEnd();
    pCmdObj->Release();
}
```



In this case, the **PlayTitle** method does not block, but the application blocks by calling **WaitForEnd**.

**Command Status Events**

If you set the DVD\_CMD\_FLAG\_SendEvents flag in the *dwFlags* parameter, the DVD Navigator sends an [**EC\_DVD\_CMD\_START**](ec-dvd-cmd-start.md) event when the command begins and an [**EC\_DVD\_CMD\_END**](ec-dvd-cmd-end.md) event when the command ends.

The event's *lParam2* parameter is the HRESULT return value for the command. The event's *lParam1* parameter provides a way get the synchronization object for the command. If you pass *lParam1* to the [**IDvdInfo2::GetCmdFromEvent**](/windows/desktop/api/Strmif/nf-strmif-idvdinfo2-getcmdfromevent) method, the method returns a pointer to the synchronization object's **IDvdCmd** interface. You can use this interface to wait for completion of the command, as described earlier. However, if you passed **NULL** for the *ppCmd* parameter in the original **IDvdControl2** method, the DVD Navigator does not create a synchronization object, and **GetCmdFromEvent** returns E\_FAIL.

The following code shows how to use command status events with no synchronization object.


```C++
hr = pDVDControl2->PlayTitle(uTitle, DVD_CMD_FLAG_SendEvents, NULL);

// In your event handling code:
switch (lEvent)
{
   case EC_DVD_CMD_END:
       HRESULT hr2 = (HRESULT)lParam2;
       /* ... */ 
       break;
}
```



Note that without a synchronization object, you cannot tell which command is associated with the event. The following code shows how to use events with the synchronization object. The idea is to store the synchronization objects in a list and then compare object pointers when you get the [**EC\_DVD\_CMD\_START**](ec-dvd-cmd-start.md) or [**EC\_DVD\_CMD\_END**](ec-dvd-cmd-end.md) event.


```C++
IDvdCmd *pCmdObj = NULL;
hr = pDVDControl2->PlayTitle(uTitle, DVD_CMD_FLAG_SendEvents, &pCmdObj);
if (SUCCEEDED(hr)) 
{
    // Store pCmdObj in a list of pending commands.
}

// In your event handling code:
switch (lEvent)
{
case EC_DVD_CMD_END:
   {
       IDvdCmd *pObj = NULL;
       hr = pDvdInfo2->GetCmdFromEvent(lParam, &pObj);
       if (SUCCEEDED(hr)) 
       {
           // Find this object in your list by comparing IUnknown
           // pointers. Assume the following function is defined in 
           // your application:
           IDvdCmd *pPendingObj = GetPendingCommandFromList(pObj); 
           if (pPendingObj)
           {
               // Update UI accordingly (not shown). 
               pPendingObj->Release();
           }
           pObj->Release();
       }
    }
    break;
} 
```



**Flushing the DVD Navigator's Buffers**

During playback, the DVD Navigator buffers video data. The amount of buffered data varies. When the DVD Navigator switches to a new piece of video, data already in the pipeline is not lost, so the transition is seamless. By default, when the DVD Navigator issues a command, it does not flush data already in the pipeline. As a result, there may be some latency before you can see the effect of the command, depending on how much data is buffered. To increase the responsiveness, you can force the DVD Navigator to flush by setting the DVD\_CMD\_FLAG\_Flush flag.


```C++
hr = pDVDControl2->PlayTitle(uTitle, DVD_CMD_FLAG_Flush, NULL);
```



This flag can be combined with any of the flags described previously, using a bitwise OR. A side effect of flushing is that some video may be lost, so do not use this flag if you need to guarantee there are no gaps in the video.

## Related topics

<dl> <dt>

[DVD Applications](dvd-applications.md)
</dt> </dl>

 

 



