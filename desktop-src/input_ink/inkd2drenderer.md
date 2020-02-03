---
Description: Implements the IInkD2DRenderer interface.
ms.assetid: d1bd910d-ce64-4424-a0e1-4f55110b0265
title: InkD2DRenderer class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- InkD2DRenderer
api_type: 
- COM
api_location: 
- Inkrenderer.idl
---

# InkD2DRenderer class

Implements the [**IInkD2DRenderer**](/windows/desktop/api/inkrenderer/nn-inkrenderer-iinkd2drenderer) interface.

An [**IInkD2DRenderer**](/windows/desktop/api/inkrenderer/nn-inkrenderer-iinkd2drenderer) object enables the rendering of ink strokes onto the designated Direct2D device context of a Universal Windows app, instead of the default [**InkCanvas**](https://msdn.microsoft.com/en-us/library/Dn858535(v=WIN.10).aspx) control.

## Members

The **InkD2DRenderer** class inherits from the [**IUnknown**](https://msdn.microsoft.com/en-us/library/ms680509(v=VS.85).aspx) interface. **InkD2DRenderer** also has these types of members:

-   [Methods](#methods)

### Methods

The **InkD2DRenderer** class has these methods.



| Method                              | Description                                                                             |
|:------------------------------------|:----------------------------------------------------------------------------------------|
| [**Draw**](https://msdn.microsoft.com/library/Mt592649(v=VS.85).aspx) | Renders the ink stroke to the designated Direct2D device context of the app.<br/> |



 

## Creation\\Access Functions

Use the following to retrieve a reference to the object:



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>[<strong>CoCreateInstance</strong>](https://msdn.microsoft.com/en-us/library/ms686615(v=VS.85).aspx)</td>
<td>Call [<strong>CoCreateInstance</strong>](https://msdn.microsoft.com/en-us/library/ms686615(v=VS.85).aspx) with the class identifier <strong>InkD2DRenderer</strong>.<br/> This snippet is taken from the &quot;InkRenderer.cpp&quot; file of the [Complex ink sample](http://go.microsoft.com/fwlink/p/?LinkID=620314).<br/> <span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>CoCreateInstance(__uuidof(InkD2DRenderer),
  nullptr,
  CLSCTX_INPROC_SERVER,
  IID_PPV_ARGS(&amp;_spInkD2DRenderer));</code></pre></td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>



 

## Examples

This snippet from the "SceneComposer.cpp" file of the [Complex ink sample](http://go.microsoft.com/fwlink/p/?LinkID=620314) demonstrates the rendering of a collection of ink strokes to a Direct2D device context.


```C++
_inkRenderer->Render(strokes, _deviceResources->GetD2DDeviceContext());
strokes->Clear();
```



This snippet from the "InkRenderer.cpp" file of the [Complex ink sample](http://go.microsoft.com/fwlink/p/?LinkID=620314) shows the Render method (called in the previous snippet) that calls the [**Draw**](https://msdn.microsoft.com/library/Mt592649(v=VS.85).aspx) method for rendering the strokes.


```C++
void InkRenderer::Render(
    Platform::Collections::Vector<
        Windows::UI::Input::Inking::InkStroke^>^ strokes,
        Microsoft::WRL::ComPtr<ID2D1DeviceContext> d2dContext)
{
    HRESULT hr = S_OK;
    if (_spInkD2DRenderer != nullptr)
    {
        if (strokes != nullptr &amp;&amp; strokes->Size > 0)
        {
            // Cast the stroke collection into IUnknown to call Inkd2dRenderer
            ComPtr<IUnknown> spUnkStrokes = 
                reinterpret_cast<IUnknown*>(reinterpret_cast<__abi_IUnknown*>(strokes));
            hr = _spInkD2DRenderer->Draw(d2dContext.Get(), spUnkStrokes.Get(), false);
            if (FAILED(hr))
            {
                DX::ThrowIfFailed(hr);
            }
        }
    }
}
```



## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | None supported<br/>                                                                  |
| Header<br/>                   | <dl> <dt>Inkrenderer.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Inkrenderer.idl</dt> </dl> |
| IID<br/>                      | IID\_IInkD2DRenderer is defined as 4044e60c-7b01-4671-a97c-04e0210a07a5<br/>         |



## See also

<dl> <dt>

[Ink renderer classes](ink-renderer-classes.md)
</dt> <dt>

[Pen and stylus interactions](https://msdn.microsoft.com/en-us/library/Mt187311(v=WIN.10).aspx)
</dt> <dt>

**Samples**
</dt> <dt>

[Ink sample](http://go.microsoft.com/fwlink/p/?LinkID=620308)
</dt> <dt>

[Simple ink sample](http://go.microsoft.com/fwlink/p/?LinkID=620312)
</dt> <dt>

[Complex ink sample](http://go.microsoft.com/fwlink/p/?LinkID=620314)
</dt> </dl>

 

 




