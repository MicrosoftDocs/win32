---
description: The following are hints and tips to consider when writing an application for TAPI 3
ms.assetid: 55aae46a-af5c-4b6d-89fc-9063f078bcd6
title: Hints and Tips
ms.topic: article
ms.date: 05/31/2018
---

# Hints and Tips

The following are hints and tips to consider when writing an application for TAPI 3:

1.  COM [**CoInitialize**](/windows/desktop/api/objbase/nf-objbase-coinitialize) indirectly creates windows; this is especially important for apartment threading. If a thread creates any windows, it must process messages. If your threads call **CoInitialize**, run a message pump to prevent problems. For example, COM might stop marshalling properly, or methods on COM interfaces, such as **IGlobalInterfaceTable** might hang.

    In apartment threading you must have a message pump regardless of whether you wait for synchronization objects. This is particularly important if you have a console application or you write a COM local/remote server object that is apartment threaded (where you do not have a console or a GUI, but the control just "runs" in the system).

    > [!Caution]  
    > When calling the wait and synchronization functions, such as [**Sleep**](/windows/desktop/api/synchapi/nf-synchapi-sleep), [**WaitForMultipleObjects**](/windows/desktop/api/synchapi/nf-synchapi-waitformultipleobjects), [**WaitForMultipleObjectsEx**](/windows/desktop/api/synchapi/nf-synchapi-waitformultipleobjectsex), [**WaitForSingleObject**](/windows/desktop/api/synchapi/nf-synchapi-waitforsingleobject), [**WaitForSingleObjectEx**](/windows/desktop/api/synchapi/nf-synchapi-waitforsingleobjectex), and so on. Instead, use [**MsgWaitForMultipleObjects**](/windows/desktop/api/winuser/nf-winuser-msgwaitformultipleobjects) and process the messages, or use [**CoWaitForMultipleHandles**](/windows/desktop/api/combaseapi/nf-combaseapi-cowaitformultiplehandles), which will automatically detect what type of apartment the thread is in (STA or MTA) and will wait either in a COM modal loop (if STA) or block on **WaitForMultipleObjects** (if MTA). **MsgWaitForMultipleObjects** and **CoWaitForMultipleHandles** also process windows messages according to the COM rules.

     

    For example, instead of:

    `Sleep (5000);`

    Use:

    ``` syntax
     {
       DWORD dwSignalled;
       HANDLE heventDone = CreateEvent(0, FALSE, FALSE, 0);

       CoWaitForMultipleHandles (COWAIT_ALERTABLE,
                             5000,
                             1,
                             &heventDone,
                             &dwSignalled);

       CloseHandle(heventDone);
     }
    ```

2.  **ITTAPIEventNotification::Event** is the apps Event function called on a TAPI 3 callback thread.

    Do the minimum in the Event routine; instead, use your own thread where possible.

    Be aware that the following code example is provided, but is not a requirement.

    ```syntax
    #include <windows.h>

    HRESULT
    STDMETHODCALLTYPE
    CTAPIEventNotification::Event(
        TAPI_EVENT TapiEvent,
        IDispatch *pEvent)
    {
        //
        // Addref the event so that it does not go away.
        //
        pEvent->AddRef();

        //
        // Post a message for reference.
        //
        BOOL RetVal = PostMessage(
                                  ghDlg,
                                  WM_PRIVATETAPIEVENT,
                                  (WPARAM) TapiEvent,
                                  (LPARAM) pEvent
                                  );

        // If (RetVal == 0 ) process error here.

        return S_OK;
    }     
    ```

3.  Do not manipulate COM objects after calling [**CoUninitialize**](/windows/desktop/api/combaseapi/nf-combaseapi-couninitialize). The results are unpredictable and detrimental to a healthy application. Some examples in which this can happen are worker threads and C++ destructors that may execute after an application calls **CoUninitialize**.

 

 
