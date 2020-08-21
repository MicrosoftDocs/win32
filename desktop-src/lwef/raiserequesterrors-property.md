---
title: RaiseRequestErrors Property
description: RaiseRequestErrors Property
ms.assetid: 60eb4478-526e-492a-8fb3-d1e54eff9868
ms.topic: article
ms.date: 05/31/2018
---

# RaiseRequestErrors Property

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns or sets whether errors for requests are raised.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.RaiseRequestErrors** \[ = *boolean*\]



| Part      | Description                                                                                                                                                                                            |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *boolean* | A Boolean value that determines whether errors in requests are raised.<br/> **True**    (Default) Request errors are raised. <br/> **False**     Request errors are not raised.<br/> |



 

</dd> </dl>

## Remarks

This property enables you to determine whether the server raises errors that occur with methods that support [**Request**](/windows/desktop/lwef/the-request-object) objects. For example, if you specify an animation name that does not exist in a [**Play**](play-method.md)method, the server raises an error (displaying the error message) unless you set this property to **False**.

It may be useful for programming languages that do not provide recovery when an error is raised. However, use care when setting this property to **False**, because it might be harder to find errors in your code.

 

