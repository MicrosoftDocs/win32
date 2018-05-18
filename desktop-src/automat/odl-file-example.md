---
title: ODL File Example
description: The following example shows the .odl file for the Lines sample file, extracted from Lines.odl.
ms.assetid: '86d64a4f-08eb-422a-bb1d-dfa868094645'
---

# ODL File Example

The following example shows the .odl file for the Lines sample file, extracted from Lines.odl.


```C++
[
   uuid(3C591B20-1F13-101B-B826-00DD01103DE1),      // LIBID_Lines.
   helpstring("Lines 1.0 Type Library"),
   lcid(0x09),
   version(1.0)
]
library Lines
{
   importlib("stdole.tlb");
   #define DISPID_NEWENUM -4

   [
      uuid(3C591B25-1F13-101B-B826-00DD01103DE1),  // IID_Ipoint.
      helpstring("Point object."),
      oleautomation,
      dual
   ]
   interface IPoint : IDispatch
   {
      [propget, helpstring("Returns and sets x coordinate.")]
      HRESULT x([out, retval] int* retval); 
      [propput, helpstring("Returns and sets x coordinate.")]
      HRESULT x([in] int Value);

      [propget, helpstring("Returns and sets y coordinate.")]
      HRESULT y([out, retval] int* retval); 
      [propput, helpstring("Returns and sets y coordinate.")]
      HRESULT y([in] int Value);
   }

// Additional interfaces omitted for brevity.

   [
      uuid(3C591B27-1F13-101B-B826-00DD01103DE1),      // IID_Ipoints.
      helpstring("Points collection."),
      oleautomation,
      dual
   ]
   interface IPoints : IDispatch
   {
      [propget, helpstring("Returns number of points in collection.")]
      HRESULT Count([out, retval] long* retval);

      [propget, id(0),
      helpstring("Given an index, returns a point in the collection.")]
      HRESULT Item([in] long Index, [out, retval] IPoint** retval);

      [propget, restricted, id(DISPID_NEWENUM)]   // Must be propget.
      HRESULT _NewEnum([out, retval] IUnknown** retval);
   }

// Additional interface omitted for brevity.

   [
      uuid(3C591B22-1F13-101B-B826-00DD01103DE1),   // IID_Iapplication
      helpstring("Application object."),
      oleautomation,
      dual
   ]
   interface IApplication : IDispatch
   {
      [propget, helpstring("Returns the application of the object.")]
      HRESULT Application(   [out, retval] IApplication** retval);

      [propget, 
      helpstring("Returns the full name of the application.")]
      HRESULT FullName([out, retval] BSTR* retval);
      [propget, id(0),
      helpstring("Returns the name of the application.")]
      HRESULT Name([out, retval] BSTR* retval);

      [propget, helpstring("Returns the parent of the object.")]
      HRESULT Parent([out, retval] IApplication** retval);

      [propput]
      HRESULT Visible([in] boolean VisibleFlag);
      [propget, helpstring
      ("Sets or returns whether the main window is visible.")]
      HRESULT Visible(   [out, retval] boolean* retval);

      [helpstring("Exits the application.")]
      HRESULT Quit();

// Additional methods omitted for brevity.

      [helpstring("Creates new Point object initialized to (0,0).")]
      HRESULT CreatePoint(   [out, retval] IPoint** retval);
   }

   [
      uuid(3C591B21-1F13-101B-B826-00DD01103DE1),   // CLSID_Lines.
      helpstring("Lines Class"),
      appobject
   ]
   coclass Lines
   {
      [default] interface IApplication;
         interface IDispatch;
   }
}
```



The example describes a library named Lines that imports the standard OLE library Stdole.tlb. The **\#define** directive defines the constant DISPID\_NEWENUM, which is needed for the **\_NewEnum** property of the IPoints collection.

The example shows declarations for three interfaces in the library: IPoint, IPoints, and IApplication. Because all three are dual interfaces, their members can be invoked through [**IDispatch**](idispatch.md) or directly through virtual function tables (VTBLs). In addition, all of their members return HRESULT values and pass their return values as [retval](retval.md) parameters. Therefore, they can support the [**IErrorInfo**](ierrorinfo.md) interface, through which they can return detailed error information in whatever way they are invoked.

The IPoint interface has two properties, X and Y, and two pairs of accessor functions to get and set the properties.

The IPoint interface is a collection of points. It supports three read-only properties, each of which has a single accessor function. The **Count** and **Item** properties return the number of points and the value of a single point, respectively. The **\_NewEnum** property, required for collection objects, returns an enumerator object for the collection. This property has the [restricted](restricted.md) attribute, indicating that it should not be invoked from a macro language.

The **IApplication** interface describes the application object. It supports the properties **Application**, **FullName**, **Name**, **Parent**, **Visible**, and **Pane**. It supports the methods **Quit**, **CreateLine**, and **CreatePoint**.

Finally, the script defines a coclass named Lines. The [appobject](appobject.md) attribute makes the members of the coclass (**IApplication** and [**IDispatch**](idispatch.md)) globally accessible in the type library. **IApplication** is defined as the [default](default.md) member, indicating that it is the programmability interface intended for use by macro languages.

 

 




