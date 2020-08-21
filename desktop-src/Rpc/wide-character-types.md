---
title: Wide-Character Types
description: Microsoft RPC supports the wide-character type wchar\_t.
ms.assetid: 1a601461-df34-456d-93e8-4cf0b655cf2c
ms.topic: article
ms.date: 05/31/2018
---

# Wide-Character Types

Microsoft RPC supports the wide-character type [**wchar\_t**](/windows/desktop/Midl/wchar-t). The wide-character type uses 2 bytes for each character. The ANSI C-language definition allows you to initialize long characters and long strings as:

``` syntax
wchar_t wcInitial = L'a';
wchar_t * pwszString = L"Hello, world";
```

 

 