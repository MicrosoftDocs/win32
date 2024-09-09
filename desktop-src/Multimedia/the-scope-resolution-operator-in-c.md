---
title: The Scope Resolution Operator in C++
description: The Scope Resolution Operator in C++
ms.assetid: 908cf2b0-41d2-442d-aba8-82f3328c72c1
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# The Scope Resolution Operator in C++

\[The feature associated with this page, [Custom File and Stream Handlers](/windows/win32/multimedia/custom-file-and-stream-handlers), is a legacy feature. It has been superseded by [MediaStreamSource class](/uwp/api/Windows.Media.Core.MediaStreamSource). **MediaStreamSource class** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaStreamSource class** instead of **Custom File and Stream Handlers**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Two colons (::) are used in C++ as a *scope resolution* operator. This operator gives you more freedom in naming your variables by letting you distinguish between variables with the same name. For example, *MyFile::Read* refers to the *Read* method of the *MyFile* class of objects, as opposed to *YourFile::Read*, which refers to a *Read* method in the *YourFile* class.

 

 




