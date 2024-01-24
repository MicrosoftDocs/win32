---
title: Implementing CSearch
description: Implementing CSearch
ms.assetid: 3041807a-e7e0-4022-ab90-a8b846bafc0e
keywords:
- Windows Media Player plug-ins,CSearch class
- plug-ins,CSearch class
- user interface plug-ins,CSearch class
- UI plug-ins,CSearch class
- CSearch class
- programming guide,user interface plug-ins
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Implementing CSearch

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **IWMPPluginUI** interface has several methods that are called by Windows Media Player at different times during the life cycle of a plug-in instance. The wizard provides basic implementations of these methods as well as the class constructor and destructor and other class methods. The Search.h file must be modified so that Windows Media Player can communicate with the UI, which is described in the next section.

For the CPluginWindow class to have access to the private member variable m\_spCore, a friend class declaration must be made inside the CSearch class definition as shown in the following code snippet:


```C++
class ATL_NO_VTABLE CSearch : 
    public CComObjectRootEx<CComSingleThreadModel>,
    public CComCoClass<CSearch, &CLSID_Search>,
    public IWMPPluginUI
{

friend class CPluginWindow;

// Rest of class definition...

}

```



## Related topics

<dl> <dt>

[**User Interface Plug-ins Programming Guide**](user-interface-plug-ins-programming-guide.md)
</dt> </dl>

 

 




