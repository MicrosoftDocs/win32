---
title: Creating Your Transform
description: Creating Your Transform
ms.assetid: '2f75d20d-0dcf-49e4-bf3d-cde124747337'
keywords: ["Windows Movie Maker,creating custom transforms", "Movie Maker,creating custom transforms", "programming guide,creating custom transforms", "creating custom transforms using COM and DirectX", "transforms,creating using COM and DirectX", "custom transforms,creating using COM and DirectX", "Component Object Model (COM),creating custom transforms", "COM (Component Object Model),creating custom transforms", "DirectX,creating custom transforms", "Active Template Library (ATL)", "ATL (Active Template Library)"]
---

# Creating Your Transform

The only requirements for creating a transform in Windows Movie Maker 6.0 are the Component Object Model (COM) and DirectX 9.

**Note** This document assumes that you will use ATL to implement COM, although this is not required. However, ATL does simplify the process of creating a transform.

**To create a transform**

1.  Create a new ATL COM project that supports Direct3D. Refer to the DirectX documentation to learn which DirectX headers and libraries must be included. The class ID GUID you specify will be used in the XML initialization file to specify this transform.
2.  Include the following Windows Movie Maker header files in your project:

    -   gputransformplugin.h
    -   GPUPipelineTime.h

    Also, link to one of the following libraries, depending on the Visual Studio version installed on your computer:

    -   GPUPipelineVC7.lib (Visual Studio .NET)
    -   GPUPipelineVC8.lib (Visual Studio 2005)

**Note** These headers and libraries are included in [Samples](samples.md).

1.  Implement [**IMediaTransform**](imediatransform.md) and all its methods. The reference section of this document describes **IMediaTransform** and what its methods must do. Your transform must always be single-threaded; it should never create worker threads. Also, a transform can handle only one media type: video.
2.  (Optional) Implement [**INotifySeek**](inotifyseek.md) to receive notifications when a user seeks within the file.
3.  (Optional) Implement [**IControlOutputSize**](icontroloutputsize.md) to enable Windows Movie Maker to specify the dimensions of the input and output buffers allocated for your transform each time [**IMediaTransform::Process**](imediatransform-process.md) is called.
4.  (Optional) Implement an [**ITransformProperties**](itransformproperties.md) member to receive parameters from an initialization XML file. This is implemented by declaring a service map with the member variable, and calling [**CreateTransformProperties**](createtransformproperties.md) when the transform's class constructor is called. The following code demonstrates these steps with an **ITransformProperties** member named **m\_pProperties** and a **CSampleEffect** class:
    ```C++
    class ATL_NO_VTABLE CSampleEffect : 
        public IMediaTransform,
        public IServiceProviderImpl<CSampleEffect>  IServiceProvider 
    {
    public:
    ...
        BEGIN_SERVICE_MAP(CSampleEffect)
            SERVICE_ENTRY_OBJECT(SID_TransformProperties, m_pProperties)
        END_SERVICE_MAP()
    CSampleEffect()
    {
        RTN_VOID_IF_FAILED(CreateTransformProperties(&amp;m_pProperties));
        RTN_VOID_IF_BADPTR(m_pProperties); 
    }
        CComPtr<ITransformProperties>    m_pProperties;
    ```

    

5.  Compile and test your transform.
6.  Create an XML initialization file that instructs Windows Movie Maker to load your transform. See [Changes to the XML Schema](changes-to-the-xml-schema.md) for details about this file.

Remember that one transform class can support several effects or transitions in Windows Movie Maker, depending on the parameters that you specify in the XML file. For instance, if you create an effect object that fades from a specified initial color to a specified end color, you can create variations of these effects by using the XML file; for example, you can create an effect object called "Fade to Black" and another called "Fade to White" by varying the XML parameter values for each effect.

## Related topics

<dl> <dt>

[**Creating Custom Transforms Using COM and DirectX**](creating-custom-transforms-using-com-and-directx.md)
</dt> </dl>

 

 




