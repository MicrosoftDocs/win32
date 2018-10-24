---
title: ID2D1SolidColorBrush SetColor methods
description: Specifies the color of this solid color brush.
ms.assetid: 2900bf72-9641-419c-b0d7-334f14f8a474
keywords:
- SetColor methods Direct2D
topic_type:
- apiref
api_location:
- D2d1.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
api_name: 
---

# ID2D1SolidColorBrush::SetColor methods

Specifies the color of this solid color brush.

### Overload list



| Method                                                                          | Description                                                |
|:--------------------------------------------------------------------------------|:-----------------------------------------------------------|
| [**SetColor(D2D1\_COLOR\_F&)**](https://msdn.microsoft.com/en-us/library/Dd372215(v=VS.85).aspx)  | Specifies the color of this solid-color brush. <br/> |
| [**SetColor(D2D1\_COLOR\_F\*)**](https://msdn.microsoft.com/en-us/library/Dd372211(v=VS.85).aspx) | Specifies the color of this solid color brush. <br/> |



## Remarks

To help create colors, Direct2D provides the [**ColorF**](https://msdn.microsoft.com/en-us/library/Dd370907(v=VS.85).aspx) class. It offers several helper methods for creating colors and provides a set or predefined colors.

## Examples

The following code shows how to use this method.


```C++
        m_pSolidColorBrush->SetColor(
            D2D1::ColorF(
                0.0f,
                intensity,
                1.0f - intensity
                ));

        hr = m_pRealization->Fill(
                m_pRT,
                m_pSolidColorBrush,
                m_useRealizations ?
                    REALIZATION_RENDER_MODE_DEFAULT :
                    REALIZATION_RENDER_MODE_FORCE_UNREALIZED
                );
```



## Requirements



|                    |                                                                                     |
|--------------------|-------------------------------------------------------------------------------------|
| Library<br/> | <dl> <dt>D2d1.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D2d1.dll</dt> </dl> |



## See also

<dl> <dt>

[**ID2D1SolidColorBrush**](https://msdn.microsoft.com/en-us/library/Dd372207(v=VS.85).aspx)
</dt> </dl>

 

 





