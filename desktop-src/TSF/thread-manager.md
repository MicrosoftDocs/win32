---
title: Thread Manager
description: The thread manager is the base component of the TSF manager.
ms.assetid: fd43b4c3-80bb-4118-a880-bdea07022c95
keywords:
- Text Services Framework (TSF),thread manager
- TSF (Text Services Framework),thread manager
- text services,thread manager
- TSF-enabled applications,thread manager
- thread manager
- TSF manager
- event notifications
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Thread Manager

The thread manager is the base component of the TSF manager. The thread manager performs common tasks related to both applications and text services (clients). These tasks include, but are not limited to, the activation and deactivation of TSF text services, the creation of document managers, and maintenance of the proper relationship between documents and the input focus. The thread manager is defined by the [ITfThreadMgr](/windows/win32/Msctf/nn-msctf-itfthreadmgr?branch=master) interface.

The majority of the interfaces and objects provided by the TSF manager can be obtained using the methods that the thread manager interface provides.

## Applications

An application creates a thread manager object by calling [CoCreateInstance](_com_cocreateinstance) with CLSID\_TFThreadMgr.

## Text Services

A text service obtains a thread manager object in the text service [ITfTextInputProcessor::Activate](/windows/win32/Msctf/nf-msctf-itftextinputprocessor-activate?branch=master) method.

## Event Notifications

The thread manager also provides event notification to clients. In TSF, event notifications are provided by means of an event sink, which is a COM object. To receive notifications from the thread manager, a client implements an [ITfThreadMgrEventSink](/windows/win32/Msctf/nn-msctf-itfthreadmgreventsink?branch=master) object and installs the event sink. The event sink is installed by querying the thread manager for IID\_ITfSource and calling [ITfSource::AdviseSink](/windows/win32/Msctf/nf-msctf-itfsource-advisesink?branch=master) with IID\_ITfThreadMgrEventSink.

## Related topics

<dl> <dt>

[ITfThreadMgr](/windows/win32/Msctf/nn-msctf-itfthreadmgr?branch=master)
</dt> <dt>

[CoCreateInstance](_com_cocreateinstance)
</dt> <dt>

[ITfTextInputProcessor::Activate](/windows/win32/Msctf/nf-msctf-itftextinputprocessor-activate?branch=master)
</dt> <dt>

[ITfThreadMgrEventSink](/windows/win32/Msctf/nn-msctf-itfthreadmgreventsink?branch=master)
</dt> <dt>

[ITfSource::AdviseSink](/windows/win32/Msctf/nf-msctf-itfsource-advisesink?branch=master)
</dt> </dl>

 

 




