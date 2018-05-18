---
title: Text Stores
description: Text Stores
ms.assetid: 'c827999a-0b74-4e5d-901e-4c2fa1d74929'
keywords: ["Text Services Framework (TSF),text stores", "TSF (Text Services Framework),text stores", "TSF-enabled applications,text stores", "text stores", "Text Services Framework (TSF),Application Character Position (ACP)", "TSF (Text Services Framework),Application Character Position (ACP)", "TSF-enabled applications,Application Character Position (ACP)", "Application Character Position (ACP)", "ACP (Application Character Position)", "Text Services Framework (TSF),anchors", "TSF (Text Services Framework),anchors", "TSF-enabled applications,anchors", "anchors", "Text Services Framework (TSF),document locks", "TSF (Text Services Framework),document locks", "TSF-enabled applications,document locks", "document locks"]
---

# Text Stores

## Application Character Position (ACP)

An ACP is the location of a character, or characters, in a text stream that is expressed as the number of characters from the start of the text stream. Because the ACP model is zero-based, the first character in a text stream has an ACP of zero. For example:


```C++
Text Stream  H | e | l | l | o |   | W | o | r | l | d
ACP          0   1   2   3   4   5   6   7   8   9   10
```



A text store implements an object that supports the [ITextStoreACP](itextstoreacp.md) interface, which enables the text stream to be expressed in an ACP. The **ITextStoreACP** interface methods use the ACP range of the text stream to modify the text.

## Anchor-Based Applications

The manager uses the ACP-based methods natively to manipulate text. However, an anchor-based approach is available for [Microsoft Active Accessibility](_msaa_microsoft_active_accessibility_start_page) clients that support [anchors](ranges.md#anchors), whereby the manager uses [ITextStoreAnchor](itextstoreanchor.md) and [ITextStoreAnchorSink](itextstoreanchorsink.md) methods to wrap the [ITextStoreACP](itextstoreacp.md) and [ITextStoreACPSink](itextstoreacpsink.md) methods.

## Document Access Control

The text store controls access to the text stream by using [document locks](document-locks.md). To read or modify the text store, the manager must first install an advise sink that supports the [ITextStoreACPSink](itextstoreacpsink.md) interface by calling the [ITextStoreACP::AdviseSink](itextstoreacp-advisesink.md) method and passing a pointer to an advise sink. The advise sink enables the manager to obtain a document locks on the text store and receive notifications when the text store is modified by something other than the manager, such as user input through the application. Advise sinks are discussed later in this topic.

## How To Initialize the Text Store

An application initializes a text store by completing the following steps:

1.  Create a thread manager object based on the [ITfThreadMgr](itfthreadmgr.md) interface by calling the [CoCreateInstance](_com_cocreateinstance) function with a pointer to a thread manager object. The following is a code example of implementing a thread manager object.
    ```C++
    hr = CoCreateInstance (CLSID_TF_ThreadMgr, NULL, CLSCTX_INPROC_SERVER, 
                            IID_ITfThreadMgr, (void**)&amp;pThreadMgr);
    ```

    

2.  Activate the thread manager object by calling the [ITfThreadMgr::Activate](itfthreadmgr-activate.md) method. This method supplies a pointer to a [client identifier](tfclientid.md) used to create a context object. The thread manager is used to implement a document manager object.
3.  Create a document manager object based on the [ITfDocumentMgr](itfdocumentmgr.md) interface by calling the [ITfThreadMgr::CreateDocumentMgr](itfthreadmgr-createdocumentmgr.md) method with a pointer to the document manager object. The document manager object is used to implement a context object that is the text store.
4.  Create a context object from the document manager by calling the [ITfDocumentMgr::CreateContext](itfdocumentmgr-createcontext.md) method with the pointer to the text store object and a pointer to the client identifier from activating the thread manager. The following is an example of creating a context object:
    ```C++
    hr = pDocumentMgr->CreateContext(m_ClientID, 0, (ITextStoreACP*)this, 
                                    &amp;pContext, pEditCookie);
    ```

    

5.  Push the context object onto the stack with the [ITfDocumentMgr::Push](itfdocumentmgr-push.md) method. The following is an example of pushing the context object onto the stack:
    ```C++
    hr = pDocumentMgr->Push(pContext);
    ```

    

## How To Modify the Text Store

The **ITfDocumentMgr::Push** method calls **ITextStoreACP::AdviseSink** with a pointer to the advise sink interface to install a new advise sink or modify an existing advise sink. The advise sink receives notifications when the text store is modified by something other than the manager, such as user input to the application. Applications must call the [ITfThreadMgrEventSink::OnSetFocus](itfthreadmgreventsink-onsetfocus.md) method when the input method obtains the focus. Other notifications to the thread manager are provided by calling to the appropriate **ITextStoreACPSink** interface methods.

However, applications should not call the **ITextStoreACPSink** interface methods in response to **ITextStoreACP** interface methods. Applications should only call **ITextStoreACPSink** interface methods when the text store is modified by something other than the manager.

The contents of the text store can be modified with a temporary input state called a [composition](compositions.md).

## Related topics

<dl> <dt>

[Anchors](ranges.md#anchors)
</dt> <dt>

[Compositions](compositions.md)
</dt> <dt>

[Document Locks](document-locks.md)
</dt> <dt>

[ITextStoreACPSink](itextstoreacpsink.md)
</dt> <dt>

[ITextStoreACP](itextstoreacp.md)
</dt> <dt>

[ITextStoreAnchor](itextstoreanchor.md)
</dt> <dt>

[ITextStoreAnchorSink](itextstoreanchorsink.md)
</dt> <dt>

[ITfDocumentMgr](itfdocumentmgr.md)
</dt> <dt>

[ITfThreadMgr](itfthreadmgr.md)
</dt> <dt>

[ITfThreadMgrEventSink::OnSetFocus](itfthreadmgreventsink-onsetfocus.md)
</dt> <dt>

[TfClientId](tfclientid.md)
</dt> <dt>

[Microsoft Active Accessibility](_msaa_microsoft_active_accessibility_start_page)
</dt> </dl>

 

 




