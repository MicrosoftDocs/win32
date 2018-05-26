---
Description: Fired before any script is executed on the page.
ms.assetid: dfb3cc08-e166-455a-b26b-e6f36b394df0
title: IWebApplicationScriptEventsBeforeScriptExecuted method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWebApplicationScriptEvents::BeforeScriptExecuted method

Fired before any script is executed on the page.

## Syntax


```C++
HRESULT BeforeScriptExecuted(
  [in] IHTMLWindow2  *htmlWindow,
  [in] IActiveScript *scriptEngine
);
```



## Parameters

<dl> <dt>

*htmlWindow* \[in\]
</dt> <dd>

Type: **[**IHTMLWindow2**](_inet_IHTMLWindow2_Interface)\***

The windows or frame that is about to execute its first script.

</dd> <dt>

*scriptEngine* \[in\]
</dt> <dd>

Type: **[**IActiveScript**](d8acee11-7f0d-4999-b97a-66774af16f71)\***

The script engine.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                          |
| IDL<br/>                      | <dl> <dt>Webapplication.idl</dt> </dl> |



## See also

<dl> <dt>

[**IWebApplicationScriptEvents**](/windows/previous-versions/webapplication/nn-webapplication-iwebapplicationscriptevents?branch=master)
</dt> </dl>

 

 




