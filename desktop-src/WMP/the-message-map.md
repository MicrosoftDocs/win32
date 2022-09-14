---
title: The Message Map
description: The Message Map
ms.assetid: 4640b0f5-625e-4a9e-86f5-3e75d0afb40d
keywords:
- Windows Media Player plug-ins,message map
- plug-ins,message map
- user interface plug-ins,message map
- UI plug-ins,message map
ms.topic: article
ms.date: 05/31/2018
---

# The Message Map

The plug-in window responds to various events by calling methods that are mapped to corresponding event messages. The wizard provides a mapping so that OnPaint and OnEraseBackground will be called at the appropriate times. To create the **Search** button and to respond to clicks from it, the message map section is modified as follows:


```C++
BEGIN_MSG_MAP(CPluginWindow)
    MESSAGE_HANDLER(WM_PAINT, OnPaint)
    MESSAGE_HANDLER(WM_ERASEBKGND, OnEraseBackground)
    MESSAGE_HANDLER(WM_CREATE, OnCreate)
    COMMAND_ID_HANDLER(IDC_SEARCH, OnSearch)
END_MSG_MAP()

```



## Related topics

<dl> <dt>

[**Implementing CPluginWindow**](implementing-cpluginwindow.md)
</dt> </dl>

 

 




