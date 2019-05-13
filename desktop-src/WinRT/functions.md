---
Description: Functions
ms.assetid: 3D60C81F-B1CC-4485-B7C3-B1C6E903865B
title: Functions
ms.topic: article
ms.date: 05/10/2019
---

# Functions

## In this section



| Function | Description |
|-|-|
| [**CoDecodeProxy**](/windows/desktop/api/combaseapi/nf-combaseapi-codecodeproxy) | Locates the implementation of a Component Object Model (COM) interface in a server process given an interface to a proxied object. |
| [**CreateControlInput**](/windows/desktop/api/corewindow/nf-corewindow-createcontrolinput) | Creates a [**ICoreInputSourceBase**](https://msdn.microsoft.com/en-us/library/Dn251603(v=WIN.10).aspx) object in the caller’s UI thread. |
| [**CreateControlInputEx**](/windows/desktop/api/corewindow/nf-corewindow-createcontrolinputex) | Creates a [**ICoreInputSourceBase**](https://msdn.microsoft.com/en-us/library/Dn251603(v=WIN.10).aspx) object in a worker thread or the UI thread.  |
| [**CreateDirect3D11DeviceFromDXGIDevice**](/windows/desktop/api/windows.graphics.directx.direct3d11.interop/nf-windows-graphics-directx-direct3d11-interop-createdirect3d11devicefromdxgidevice) | Creates an instance of IDirect3DDevice from an IDXGIDevice. |
| [**CreateDirect3D11SurfaceFromDXGISurface**](/windows/desktop/api/windows.graphics.directx.direct3d11.interop/nf-windows-graphics-directx-direct3d11-interop-createdirect3d11surfacefromdxgisurface) | Creates an instance of IDirect3DSurface from an IDXGISurface. |
| [**CreateDirect3DDevice**](/windows/desktop/api/windows.graphics.directx.direct3d11.interop/nf-windows-graphics-directx-direct3d11-interop-createdirect3ddevice) | Creates an instance of [IDirect3DDevice](/uwp/api/windows.graphics.directx.direct3d11.idirect3ddevice) from an [IDXGIDevice](/windows/desktop/api/dxgi/nn-dxgi-idxgidevice). |
| [**CreateDirect3DSurface**](/windows/desktop/api/windows.graphics.directx.direct3d11.interop/nf-windows-graphics-directx-direct3d11-interop-createdirect3dsurface) | Creates an instance of [IDirect3DSurface](/uwp/api/windows.graphics.directx.direct3d11.idirect3dsurface) from an [IDXGISurface](/windows/desktop/api/dxgi/nn-dxgi-idxgisurface). |
| [**CreateRandomAccessStreamOnFile**](https://msdn.microsoft.com/en-us/library/Hh846256(v=VS.85).aspx) | Creates a Windows Runtime random access stream for a file. |
| [**CreateRandomAccessStreamOverStream**](https://msdn.microsoft.com/en-us/library/Hh846257(v=VS.85).aspx) | Creates a Windows Runtime random access stream around an [**IStream**](https://msdn.microsoft.com/en-us/library/Aa380034(v=VS.85).aspx) base implementation. |
| [**CreateStreamOverRandomAccessStream**](https://msdn.microsoft.com/en-us/library/Hh846258(v=VS.85).aspx) | Creates an [**IStream**](https://msdn.microsoft.com/en-us/library/Aa380034(v=VS.85).aspx) around a Windows Runtime [**IRandomAccessStream**](https://msdn.microsoft.com/en-us/library/Hh438400(v=VS.85).aspx) object. |
| [**CreateXamlUIPresenter**](createxamluipresenter.md) | A static creator function that can create a [**XamlUIPresenter**](https://msdn.microsoft.com/en-us/library/Hh701914(v=WIN.10).aspx) for a render surface in a desktop app. |
| [**DbgRaiseAssertionFailure**](https://msdn.microsoft.com/en-us/library/JJ635749(v=VS.85).aspx) | Raises an assert for debugging.  |
| [**GetDXGIInterface(IDirect3DDevice^, DXGI_TYPE**)**](/windows/desktop/api/windows.graphics.directx.direct3d11.interop/nf-windows-graphics-directx-direct3d11-interop-getdxgiinterface) | Retrieves a DXGI interface from an [IDirect3DDevice](/uwp/api/windows.graphics.directx.direct3d11.idirect3ddevice) instance. |
| [**GetDXGIInterface(IDirect3DSurface^, DXGI_TYPE**)**](/windows/desktop/api/windows.graphics.directx.direct3d11.interop/nf-windows-graphics-directx-direct3d11-interop-getdxgiinterface~r1) | Retrieves a DXGI interface from an [IDirect3DSurface](/uwp/api/windows.graphics.directx.direct3d11.idirect3dsurface) instance. |
| [**GetDXGIInterfaceFromObject**](/windows/desktop/api/windows.graphics.directx.direct3d11.interop/nf-windows-graphics-directx-direct3d11-interop-getdxgiinterfacefromobject) | Retrieves a DXGI interface from an object. |
| [**GetRestrictedErrorInfo**](https://msdn.microsoft.com/en-us/library/JJ219013(v=VS.85).aspx) | Gets the restricted error information object set by a previous call to [**SetRestrictedErrorInfo**](https://msdn.microsoft.com/en-us/library/JJ219016(v=VS.85).aspx) in the current logical thread. |
| [**HSTRING\_UserFree**](https://msdn.microsoft.com/en-us/library/Hh846259(v=VS.85).aspx) | Frees resources on the server side when called by RPC stub files. |
| [**HSTRING\_UserFree64**](https://msdn.microsoft.com/en-us/library/Hh846260(v=VS.85).aspx) | Frees resources on the server side when called by RPC stub files.  |
| [**HSTRING\_UserMarshal**](https://msdn.microsoft.com/en-us/library/Hh846261(v=VS.85).aspx) | Marshals an [**HSTRING**](hstring.md) object into the RPC buffer. |
| [**HSTRING\_UserMarshal64**](https://msdn.microsoft.com/en-us/library/Hh846262(v=VS.85).aspx) | Marshals an [**HSTRING**](hstring.md) object into the RPC buffer. |
| [**HSTRING\_UserSize**](https://msdn.microsoft.com/en-us/library/Hh846263(v=VS.85).aspx) | Calculates the wire size of the [**HSTRING**](hstring.md) object, and gets its handle and data. |
| [**HSTRING\_UserSize64**](https://msdn.microsoft.com/en-us/library/Hh846264(v=VS.85).aspx) | Calculates the wire size of the [**HSTRING**](hstring.md) object, and gets its handle and data. |
| [**HSTRING\_UserUnmarshal**](https://msdn.microsoft.com/en-us/library/Hh846265(v=VS.85).aspx) | Unmarshals an [**HSTRING**](hstring.md) object from the RPC buffer. |
| [**HSTRING\_UserUnmarshal64**](https://msdn.microsoft.com/en-us/library/Hh846266(v=VS.85).aspx) | Unmarshals an [**HSTRING**](hstring.md) object from the RPC buffer. |
| [**IsErrorPropagationEnabled**](https://msdn.microsoft.com/en-us/library/Dn975143(v=VS.85).aspx) | Indicates whether the [**CoreApplication.UnhandledErrorDetected**](https://msdn.microsoft.com/en-us/library/Dn297297(v=WIN.10).aspx) event occurs for the errors that are returned by the delegate registered as a callback function for a Windows Runtime API event or the completion of an asynchronous method. |
| [**DllGetActivationFactory**](https://msdn.microsoft.com/en-us/library/BR205771(v=VS.85).aspx) | Retrieves the activation factory from a DLL that contains activatable Windows Runtime classes. |
| [**MetaDataGetDispenser**](https://msdn.microsoft.com/en-us/library/BR229853(v=VS.85).aspx) | Creates a dispenser class. |
| [**PdfCreateRenderer**](/windows/desktop/api/windows.data.pdf.interop/nf-windows-data-pdf-interop-pdfcreaterenderer) | Gets an instance of the [**IPdfRendererNative**](/windows/desktop/api/windows.data.pdf.interop/nn-windows-data-pdf-interop-ipdfrenderernative) interface for displaying a single page of a Portable Document Format (PDF) file. |
| [**PdfRenderParams**](/windows/desktop/api/windows.data.pdf.interop/nf-windows-data-pdf-interop-pdfrenderparams) | Populates a [**PDF\_RENDER\_PARAMS**](/windows/desktop/api/windows.data.pdf.interop/ns-windows-data-pdf-interop-pdf_render_params) stucture. A PDF\_RENDER\_PARAMS structure represents a set of properties for outputting a single page of a PDF file. |
| [**RoActivateInstance**](https://msdn.microsoft.com/en-us/library/BR224646(v=VS.85).aspx) | Activates the specified Windows Runtime class. |
| [**RoCaptureErrorContext**](https://msdn.microsoft.com/en-us/library/JJ219014(v=VS.85).aspx) | Saves the current error context so that it's available for later calls to the [**RoFailFastWithErrorContext**](https://msdn.microsoft.com/en-us/library/JJ219015(v=VS.85).aspx) function. |
| [**RoClearError**](https://msdn.microsoft.com/en-us/library/Dn302148(v=VS.85).aspx) | Removes existing error information from the current thread environment block (TEB). |
| [**RoFailFastWithErrorContext**](https://msdn.microsoft.com/en-us/library/JJ219015(v=VS.85).aspx) | Raises a non-continuable exception in the current process. |
| [**RoFreeParameterizedTypeExtra**](https://msdn.microsoft.com/en-us/library/BR229854(v=VS.85).aspx) | Frees the handle allocated by [**RoGetParameterizedTypeInstanceIID**](https://msdn.microsoft.com/en-us/library/BR229857(v=VS.85).aspx). |
| [**RoGetActivatableClassRegistration**](https://msdn.microsoft.com/en-us/library/BR229855(v=VS.85).aspx) | Enables retrieving class registration information. |
| [**RoGetActivationFactory**](https://msdn.microsoft.com/en-us/library/BR224648(v=VS.85).aspx) | Gets the activation factory for the specified runtime class. |
| [**RoGetAgileReference**](/windows/desktop/api/ComBaseApi/nf-combaseapi-rogetagilereference) | Creates an agile reference for an object specified by the given interface. |
| [**RoGetApartmentIdentifier**](https://msdn.microsoft.com/en-us/library/JJ219266(v=VS.85).aspx) | Gets a unique identifier for the current apartment. |
| [**RoGetBufferMarshaler**](https://msdn.microsoft.com/en-us/library/Hh438433(v=VS.85).aspx) | Provides a standard IBuffer marshaler to implement the semantics associated with the IBuffer interface when it is marshaled. |
| [**RoGetErrorReportingFlags**](https://msdn.microsoft.com/en-us/library/BR224649(v=VS.85).aspx) | Gets the current reporting behavior of Windows Runtime error functions. |
| [**RoGetMetaDataFile**](https://msdn.microsoft.com/en-us/library/BR229856(v=VS.85).aspx) | Locates and retrieves the metadata file that describes the Application Binary Interface (ABI) for the specified typename. |
| [**RoGetParameterizedTypeInstanceIID**](https://msdn.microsoft.com/en-us/library/BR229857(v=VS.85).aspx) | Computes the interface identifier (IID) of the interface or delegate type that results when a parameterized interface or delegate is instantiated with the specified type arguments. |
| [**RoGetServerActivatableClasses**](https://msdn.microsoft.com/en-us/library/BR229858(v=VS.85).aspx) | Retrieves the activatable classes that are registered for a given executable (EXE) server, which was registered under the package ID of the calling process. |
| [**RoInitialize**](https://msdn.microsoft.com/en-us/library/BR224650(v=VS.85).aspx) | Initializes the Windows Runtime on the current thread with the specified concurrency model. |
| [**RoInspectThreadErrorInfo**](https://msdn.microsoft.com/en-us/library/Dn302171(v=VS.85).aspx) | Gets the error object that represents the call stack at the point where the error originated |
| [**RoInspectCapturedStackBackTrace**](https://msdn.microsoft.com/en-us/library/Dn302149(v=VS.85).aspx) | Provides a way to for debuggers to inspect a call stack from a target process. |
| [**RoOriginateError**](https://msdn.microsoft.com/en-us/library/BR224651(v=VS.85).aspx) | Reports an error and an informative string to an attached debugger. |
| [**RoOriginateErrorW**](https://msdn.microsoft.com/en-us/library/BR224652(v=VS.85).aspx) | Reports an error and an informative string to an attached debugger. |
| [**RoOriginateLanguageException**](https://msdn.microsoft.com/en-us/library/Dn302172(v=VS.85).aspx) | Reports an error, an informative string, and an error object to an attached debugger. |
| [**RoParameterizedTypeExtraGetTypeSignature**](https://msdn.microsoft.com/en-us/library/BR229859(v=VS.85).aspx) | Gets the type signature used to compute the IID from the last call to [**RoGetParameterizedTypeInstanceIID**](https://msdn.microsoft.com/en-us/library/BR229857(v=VS.85).aspx) with the specified handle. |
| [**RoParseTypeName**](https://msdn.microsoft.com/en-us/library/Hh438434(v=VS.85).aspx) | Parses a type name and existing type parameters, in the case of parameterized types. |
| [**RoRegisterActivationFactories**](https://msdn.microsoft.com/en-us/library/BR224653(v=VS.85).aspx) | Registers an array out-of-process activation factories for a Windows Runtime exe server. |
| [**RoRegisterForApartmentShutdown**](https://msdn.microsoft.com/en-us/library/JJ219267(v=VS.85).aspx) | Registers an [**IApartmentShutdown**](/windows/desktop/api/objidl/nn-objidl-iapartmentshutdown) callback to be invoked when the current apartment shuts down. |
| [**RoReportUnhandledError**](https://msdn.microsoft.com/en-us/library/Dn457328(v=VS.85).aspx) | Triggers the Global Error Handler when an unhandled exception occurs. |
| [**RoReportFailedDelegate**](https://msdn.microsoft.com/en-us/library/Dn957499(v=VS.85).aspx) | Triggers the Global Error Handler when a delegate failure occurs. |
| [**RoResolveNamespace**](https://msdn.microsoft.com/en-us/library/BR229860(v=VS.85).aspx) | Determine the direct children, types, and sub-namespaces of the specified Windows Runtime namespace, from any programming language supported by the Windows Runtime. |
| [**RoResolveRestrictedErrorInfoReference**](https://msdn.microsoft.com/en-us/library/BR229861(v=VS.85).aspx) | Returns the [**IRestrictedErrorInfo**](/windows/desktop/api/RestrictedErrorInfo/nn-restrictederrorinfo-irestrictederrorinfo) interface pointer based on the given reference. |
| [**RoRevokeActivationFactories**](https://msdn.microsoft.com/en-us/library/BR224655(v=VS.85).aspx) | Removes an array of registered activation factories from the Windows Runtime. |
| [**RoSetErrorReportingFlags**](https://msdn.microsoft.com/en-us/library/BR224657(v=VS.85).aspx) | Sets the reporting behavior of Windows Runtime error functions. |
| [**RoTransformError**](https://msdn.microsoft.com/en-us/library/BR224658(v=VS.85).aspx) | Reports a modified error and an informative string to an attached debugger. |
| [**RoTransformErrorW**](https://msdn.microsoft.com/en-us/library/BR224659(v=VS.85).aspx) | Reports a transformed error and an informative string to an attached debugger. |
| [**RoUninitialize**](https://msdn.microsoft.com/en-us/library/BR224660(v=VS.85).aspx) | Closes the Windows Runtime on the current thread. |
| [**RoUnregisterForApartmentShutdown**](https://msdn.microsoft.com/en-us/library/JJ219268(v=VS.85).aspx) | Unregisters a previously registered [**IApartmentShutdown**](/windows/desktop/api/objidl/nn-objidl-iapartmentshutdown) interface. |
| [**SetRestrictedErrorInfo**](https://msdn.microsoft.com/en-us/library/JJ219016(v=VS.85).aspx) | Sets the restricted error information object for the current thread. |
| [**WindowsCompareStringOrdinal**](https://msdn.microsoft.com/en-us/library/BR224628(v=VS.85).aspx) | Compares two specified [**HSTRING**](hstring.md) objects and returns an integer that indicates their relative position in a sort order. |
| [**WindowsConcatString**](https://msdn.microsoft.com/en-us/library/BR224629(v=VS.85).aspx) | Concatenates two specified strings. |
| [**WindowsCreateString**](https://msdn.microsoft.com/en-us/library/BR224630(v=VS.85).aspx) | Creates a new [**HSTRING**](hstring.md) based on the specified source string. |
| [**WindowsCreateStringReference**](https://msdn.microsoft.com/en-us/library/BR224631(v=VS.85).aspx) | Creates a new string reference based on the specified string. |
| [**WindowsDeleteString**](https://msdn.microsoft.com/en-us/library/BR224632(v=VS.85).aspx) | Decrements the reference count of a string buffer. |
| [**WindowsDeleteStringBuffer**](https://msdn.microsoft.com/en-us/library/BR224633(v=VS.85).aspx) | Discards a preallocated string buffer if it was not promoted to an [**HSTRING**](hstring.md). |
| [**WindowsDuplicateString**](https://msdn.microsoft.com/en-us/library/BR224634(v=VS.85).aspx) | Creates a copy of the specified string. |
| [**WindowsGetStringLen**](https://msdn.microsoft.com/en-us/library/BR224635(v=VS.85).aspx) | Gets the length, in Unicode characters, of the specified string. |
| [**WindowsGetStringRawBuffer**](https://msdn.microsoft.com/en-us/library/BR224636(v=VS.85).aspx) | Gets the backing buffer for the specified string. |
| [**WindowsInspectString**](https://msdn.microsoft.com/en-us/library/Hh438435(v=VS.85).aspx) | Provides a way to for debuggers to display the value of an Windows Runtime [**HSTRING**](hstring.md) in another address space, remotely, or from a dump.  |
| [**WindowsInspectString2**](https://msdn.microsoft.com/en-us/library/Mt829377(v=VS.85).aspx) | Provides a way to for debuggers to display the value of an Windows Runtime [**HSTRING**](hstring.md) in another address space, remotely, or from a dump.  |
| [**WindowsIsStringEmpty**](https://msdn.microsoft.com/en-us/library/BR224637(v=VS.85).aspx) | Indicates whether the specified string is the empty string. |
| [**WindowsPreallocateStringBuffer**](https://msdn.microsoft.com/en-us/library/BR224638(v=VS.85).aspx) | Allocates a mutable character buffer for use in [**HSTRING**](hstring.md) creation. |
| [**WindowsPromoteStringBuffer**](https://msdn.microsoft.com/en-us/library/BR224639(v=VS.85).aspx) | Creates an [**HSTRING**](hstring.md) from the specified [**HSTRING\_BUFFER**](hstring-buffer.md). |
| [**WindowsReplaceString**](https://msdn.microsoft.com/en-us/library/BR224640(v=VS.85).aspx) | Replaces all occurrences of a set of characters in the specified string with another set of characters to create a new string. |
| [**WindowsStringHasEmbeddedNull**](https://msdn.microsoft.com/en-us/library/BR224641(v=VS.85).aspx) | Indicates whether the specified string has embedded null characters. |
| [**WindowsSubstring**](https://msdn.microsoft.com/en-us/library/BR224642(v=VS.85).aspx) | Retrieves a substring from the specified string. The substring starts at the specified character position. |
| [**WindowsSubstringWithSpecifiedLength**](https://msdn.microsoft.com/en-us/library/BR224643(v=VS.85).aspx) | Retrieves a substring from the specified string. The substring starts at a specified character position and has a specified length. |
| [**WindowsTrimStringEnd**](https://msdn.microsoft.com/en-us/library/BR224644(v=VS.85).aspx) | Removes all trailing occurrences of a specified set of characters from the source string. |
| [**WindowsTrimStringStart**](https://msdn.microsoft.com/en-us/library/BR224645(v=VS.85).aspx) | Removes all leading occurrences of a specified set of characters from the source string. |



 

 

 




