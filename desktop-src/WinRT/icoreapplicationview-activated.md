---
description: Occurs when a Windows Store app is activated.
ms.assetid: CA0DB2D4-3417-48F5-8455-D87D0F323A1E
title: ICoreApplicationView::Activated event (Windows.ApplicationModel.Core.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ICoreApplicationView::Activated event

Occurs when a Windows Store app is activated.

## Syntax


```C++
void Activated(
  [in] ITypedEventHandler<ICoreApplicationView*, IActivatedEventArgs*> handler
);
```



## Parameters

<dl> <dt>

*handler* \[in\]
</dt> <dd></dd> </dl>

## Return value

This event does not return a value.

## Remarks

Do not call the [**Exit**](/previous-versions//hh438368(v=vs.85)) method from within *handler*.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                               |
| Header<br/>                   | <dl> <dt>Windows.ApplicationModel.Core.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Windows.ApplicationModel.Core.idl</dt> </dl> |



 

 
