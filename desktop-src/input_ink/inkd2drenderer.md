---
description: Implements the IInkD2DRenderer interface.
ms.assetid: d1bd910d-ce64-4424-a0e1-4f55110b0265
title: InkD2DRenderer class
ms.topic: language-reference
ms.date: 02/03/2020
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

Implements the [**IInkD2DRenderer**](/windows/win32/api/inkrenderer/nn-inkrenderer-iinkd2drenderer) interface.

An [**IInkD2DRenderer**](/windows/win32/api/inkrenderer/nn-inkrenderer-iinkd2drenderer) object enables the rendering of ink strokes onto the designated Direct2D device context of a Universal Windows app, instead of the default [**InkCanvas**](/uwp/api/Windows.UI.Xaml.Controls.InkCanvas) control.

## Members

The **InkD2DRenderer** class inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **InkD2DRenderer** also has these types of members:

- [Methods](#methods)

### Methods

The **InkD2DRenderer** class has these methods.

| Method                              | Description                                                                             |
|:------------------------------------|:----------------------------------------------------------------------------------------|
| [**Draw**](/windows/win32/api/inkrenderer/nf-inkrenderer-iinkd2drenderer-draw) | Renders the ink stroke to the designated Direct2D device context of the app.<br/> |

## Creation\\Access Functions

Call [<strong>CoCreateInstance</strong>](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) with the class identifier <strong>InkD2DRenderer</strong> to retrieve a reference to the object.

``` C++
CoCreateInstance(__uuidof(InkD2DRenderer),
  nullptr,
  CLSCTX_INPROC_SERVER,
  IID_PPV_ARGS(&_spInkD2DRenderer));
```

## Examples

This snippet from the "SceneComposer.cpp" file of the [Complex inking sample](/samples/microsoft/windows-universal-samples/complexink/) demonstrates the rendering of a collection of ink strokes to a Direct2D device context.

```C++
_inkRenderer->Render(strokes, _deviceResources->GetD2DDeviceContext());
strokes->Clear();
```

This snippet from the "InkRenderer.cpp" file of the [Complex inking sample](/samples/microsoft/windows-universal-samples/complexink/) shows the Render method (called in the previous snippet) that calls the [**Draw**](/windows/win32/api/inkrenderer/nf-inkrenderer-iinkd2drenderer-draw) method for rendering the strokes.

```C++
void InkRenderer::Render(
    Platform::Collections::Vector<
        Windows::UI::Input::Inking::InkStroke^>^ strokes,
        Microsoft::WRL::ComPtr<ID2D1DeviceContext> d2dContext)
{
    HRESULT hr = S_OK;
    if (_spInkD2DRenderer != nullptr)
    {
        if (strokes != nullptr && strokes->Size > 0)
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

| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | None supported<br/>                                                                  |
| Header<br/>                   | <dl> <dt>Inkrenderer.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Inkrenderer.idl</dt> </dl> |
| IID<br/>                      | IID\_IInkD2DRenderer is defined as 4044e60c-7b01-4671-a97c-04e0210a07a5<br/>         |

## Related topics

[Ink renderer](ink-renderer.md), [Pen and stylus interactions](/windows/uwp/design/input/pen-and-stylus-interactions), [Ink Analysis sample](/samples/microsoft/windows-universal-samples/inkanalysis/), [Simple inking sample](/samples/microsoft/windows-universal-samples/simpleink/), [Complex inking sample](/samples/microsoft/windows-universal-samples/complexink/)
