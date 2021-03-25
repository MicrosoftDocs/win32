---
description: A reference for Windows Runtime C++ functions.
ms.assetid: 3D60C81F-B1CC-4485-B7C3-B1C6E903865B

title: Functions (Windows Runtime)

ms.topic: article
ms.date: 05/10/2019
---

# Functions (Windows Runtime C++ reference)

## In this section



| Function | Description |
|-|-|
| [**CoDecodeProxy**](/windows/desktop/api/combaseapi/nf-combaseapi-codecodeproxy) | Locates the implementation of a Component Object Model (COM) interface in a server process given an interface to a proxied object. |
| [**CreateControlInput**](/windows/desktop/api/corewindow/nf-corewindow-createcontrolinput) | Creates a [**ICoreInputSourceBase**](/uwp/api/Windows.UI.Core.ICoreInputSourceBase?view=winrt-19041) object in the caller’s UI thread. |
| [**CreateControlInputEx**](/windows/desktop/api/corewindow/nf-corewindow-createcontrolinputex) | Creates a [**ICoreInputSourceBase**](/uwp/api/Windows.UI.Core.ICoreInputSourceBase?view=winrt-19041) object in a worker thread or the UI thread.  |
| [**CreateDirect3D11DeviceFromDXGIDevice**](/windows/desktop/api/windows.graphics.directx.direct3d11.interop/nf-windows-graphics-directx-direct3d11-interop-createdirect3d11devicefromdxgidevice) | Creates an instance of IDirect3DDevice from an IDXGIDevice. |
| [**CreateDirect3D11SurfaceFromDXGISurface**](/windows/desktop/api/windows.graphics.directx.direct3d11.interop/nf-windows-graphics-directx-direct3d11-interop-createdirect3d11surfacefromdxgisurface) | Creates an instance of IDirect3DSurface from an IDXGISurface. |
| [**CreateDirect3DDevice**](/windows/desktop/api/windows.graphics.directx.direct3d11.interop/nf-windows-graphics-directx-direct3d11-interop-createdirect3ddevice) | Creates an instance of [IDirect3DDevice](/uwp/api/windows.graphics.directx.direct3d11.idirect3ddevice) from an [IDXGIDevice](/windows/desktop/api/dxgi/nn-dxgi-idxgidevice). |
| [**CreateDirect3DSurface**](/windows/desktop/api/windows.graphics.directx.direct3d11.interop/nf-windows-graphics-directx-direct3d11-interop-createdirect3dsurface) | Creates an instance of [IDirect3DSurface](/uwp/api/windows.graphics.directx.direct3d11.idirect3dsurface) from an [IDXGISurface](/windows/desktop/api/dxgi/nn-dxgi-idxgisurface). |
| [**CreateRandomAccessStreamOnFile**](/windows/win32/api/shcore/nf-shcore-createrandomaccessstreamonfile) | Creates a Windows Runtime random access stream for a file. |
| [**CreateRandomAccessStreamOverStream**](/windows/win32/api/shcore/nf-shcore-createrandomaccessstreamoverstream) | Creates a Windows Runtime random access stream around an [**IStream**](/windows/win32/api/objidl/nn-objidl-istream) base implementation. |
| [**CreateStreamOverRandomAccessStream**](/windows/win32/api/shcore/nf-shcore-createstreamoverrandomaccessstream) | Creates an [**IStream**](/windows/win32/api/objidl/nn-objidl-istream) around a Windows Runtime [**IRandomAccessStream**](/previous-versions//hh438400(v=vs.85)) object. |
| [**CreateXamlUIPresenter**](createxamluipresenter.md) | A static creator function that can create a [**XamlUIPresenter**](/uwp/api/Windows.UI.Xaml.Hosting.XamlUIPresenter?view=winrt-19041) for a render surface in a desktop app. |
| [**DbgRaiseAssertionFailure**](/previous-versions//jj635749(v=vs.85)) | Raises an assert for debugging.  |
| [**GetDXGIInterface(IDirect3DDevice^, DXGI_TYPE**)**](/windows/desktop/api/windows.graphics.directx.direct3d11.interop/nf-windows-graphics-directx-direct3d11-interop-getdxgiinterface) | Retrieves a DXGI interface from an [IDirect3DDevice](/uwp/api/windows.graphics.directx.direct3d11.idirect3ddevice) instance. |
| [**GetDXGIInterface(IDirect3DSurface^, DXGI_TYPE**)**](/windows/desktop/api/windows.graphics.directx.direct3d11.interop/nf-windows-graphics-directx-direct3d11-interop-getdxgiinterface-r1) | Retrieves a DXGI interface from an [IDirect3DSurface](/uwp/api/windows.graphics.directx.direct3d11.idirect3dsurface) instance. |
| [**GetDXGIInterfaceFromObject**](/windows/desktop/api/windows.graphics.directx.direct3d11.interop/nf-windows-graphics-directx-direct3d11-interop-getdxgiinterfacefromobject) | Retrieves a DXGI interface from an object. |
| [**GetRestrictedErrorInfo**](/windows/win32/api/roerrorapi/nf-roerrorapi-getrestrictederrorinfo) | Gets the restricted error information object set by a previous call to [**SetRestrictedErrorInfo**](/windows/win32/api/roerrorapi/nf-roerrorapi-setrestrictederrorinfo) in the current logical thread. |
| [**HSTRING\_UserFree**](/windows/win32/api/inspectable/nf-inspectable-hstring_userfree) | Frees resources on the server side when called by RPC stub files. |
| [**HSTRING\_UserFree64**](/windows/win32/api/inspectable/nf-inspectable-hstring_userfree64) | Frees resources on the server side when called by RPC stub files.  |
| [**HSTRING\_UserMarshal**](/windows/win32/api/inspectable/nf-inspectable-hstring_usermarshal) | Marshals an [**HSTRING**](hstring.md) object into the RPC buffer. |
| [**HSTRING\_UserMarshal64**](/windows/win32/api/inspectable/nf-inspectable-hstring_usermarshal64) | Marshals an [**HSTRING**](hstring.md) object into the RPC buffer. |
| [**HSTRING\_UserSize**](/windows/win32/api/inspectable/nf-inspectable-hstring_usersize) | Calculates the wire size of the [**HSTRING**](hstring.md) object, and gets its handle and data. |
| [**HSTRING\_UserSize64**](/windows/win32/api/inspectable/nf-inspectable-hstring_usersize64) | Calculates the wire size of the [**HSTRING**](hstring.md) object, and gets its handle and data. |
| [**HSTRING\_UserUnmarshal**](/windows/win32/api/inspectable/nf-inspectable-hstring_userunmarshal) | Unmarshals an [**HSTRING**](hstring.md) object from the RPC buffer. |
| [**HSTRING\_UserUnmarshal64**](/windows/win32/api/inspectable/nf-inspectable-hstring_userunmarshal64) | Unmarshals an [**HSTRING**](hstring.md) object from the RPC buffer. |
| [**IsErrorPropagationEnabled**](/windows/win32/api/roerrorapi/nf-roerrorapi-iserrorpropagationenabled) | Indicates whether the [**CoreApplication.UnhandledErrorDetected**](/uwp/api/Windows.ApplicationModel.Core.CoreApplication?view=winrt-19041) event occurs for the errors that are returned by the delegate registered as a callback function for a Windows Runtime API event or the completion of an asynchronous method. |
| [**DllGetActivationFactory**](/previous-versions//br205771(v=vs.85)) | Retrieves the activation factory from a DLL that contains activatable Windows Runtime classes. |
| [**MetaDataGetDispenser**](/windows/win32/api/rometadata/nf-rometadata-metadatagetdispenser) | Creates a dispenser class. |
| [**PdfCreateRenderer**](/windows/desktop/api/windows.data.pdf.interop/nf-windows-data-pdf-interop-pdfcreaterenderer) | Gets an instance of the [**IPdfRendererNative**](/windows/desktop/api/windows.data.pdf.interop/nn-windows-data-pdf-interop-ipdfrenderernative) interface for displaying a single page of a Portable Document Format (PDF) file. |
| [**PdfRenderParams**](/windows/desktop/api/windows.data.pdf.interop/nf-windows-data-pdf-interop-pdfrenderparams) | Populates a [**PDF\_RENDER\_PARAMS**](/windows/desktop/api/windows.data.pdf.interop/ns-windows-data-pdf-interop-pdf_render_params) stucture. A PDF\_RENDER\_PARAMS structure represents a set of properties for outputting a single page of a PDF file. |
| [**RoActivateInstance**](/windows/win32/api/roapi/nf-roapi-roactivateinstance) | Activates the specified Windows Runtime class. |
| [**RoCaptureErrorContext**](/windows/win32/api/roerrorapi/nf-roerrorapi-rocaptureerrorcontext) | Saves the current error context so that it's available for later calls to the [**RoFailFastWithErrorContext**](/windows/win32/api/roerrorapi/nf-roerrorapi-rofailfastwitherrorcontext) function. |
| [**RoClearError**](/windows/win32/api/roerrorapi/nf-roerrorapi-roclearerror) | Removes existing error information from the current thread environment block (TEB). |
| [**RoFailFastWithErrorContext**](/windows/win32/api/roerrorapi/nf-roerrorapi-rofailfastwitherrorcontext) | Raises a non-continuable exception in the current process. |
| [**RoFailFastWithErrorContextInternal2**](./roerrorapi/nf-roerrorapi-rofailfastwitherrorcontextinternal2.md) | Raises a non-continuable exception in the current process, and also allows you to include additional error context not already captured by the OS. |
| [**RoFreeParameterizedTypeExtra**](/windows/win32/api/roparameterizediid/nf-roparameterizediid-rofreeparameterizedtypeextra) | Frees the handle allocated by [**RoGetParameterizedTypeInstanceIID**](/windows/win32/api/roparameterizediid/nf-roparameterizediid-rogetparameterizedtypeinstanceiid). |
| [**RoGetActivatableClassRegistration**](/windows/win32/api/roregistrationapi/nf-roregistrationapi-rogetactivatableclassregistration) | Enables retrieving class registration information. |
| [**RoGetActivationFactory**](/windows/win32/api/roapi/nf-roapi-rogetactivationfactory) | Gets the activation factory for the specified runtime class. |
| [**RoGetAgileReference**](/windows/desktop/api/ComBaseApi/nf-combaseapi-rogetagilereference) | Creates an agile reference for an object specified by the given interface. |
| [**RoGetApartmentIdentifier**](/windows/win32/api/roapi/nf-roapi-rogetapartmentidentifier) | Gets a unique identifier for the current apartment. |
| [**RoGetBufferMarshaler**](/windows/win32/api/robuffer/nf-robuffer-rogetbuffermarshaler) | Provides a standard IBuffer marshaler to implement the semantics associated with the IBuffer interface when it is marshaled. |
| [**RoGetErrorReportingFlags**](/windows/win32/api/roerrorapi/nf-roerrorapi-rogeterrorreportingflags) | Gets the current reporting behavior of Windows Runtime error functions. |
| [**RoGetMetaDataFile**](/windows/win32/api/rometadataresolution/nf-rometadataresolution-rogetmetadatafile) | Locates and retrieves the metadata file that describes the Application Binary Interface (ABI) for the specified typename. |
| [**RoGetParameterizedTypeInstanceIID**](/windows/win32/api/roparameterizediid/nf-roparameterizediid-rogetparameterizedtypeinstanceiid) | Computes the interface identifier (IID) of the interface or delegate type that results when a parameterized interface or delegate is instantiated with the specified type arguments. |
| [**RoGetServerActivatableClasses**](/windows/win32/api/roregistrationapi/nf-roregistrationapi-rogetserveractivatableclasses) | Retrieves the activatable classes that are registered for a given executable (EXE) server, which was registered under the package ID of the calling process. |
| [**RoInitialize**](/windows/win32/api/roapi/nf-roapi-roinitialize) | Initializes the Windows Runtime on the current thread with the specified concurrency model. |
| [**RoInspectThreadErrorInfo**](/windows/win32/api/roerrorapi/nf-roerrorapi-roinspectthreaderrorinfo) | Gets the error object that represents the call stack at the point where the error originated |
| [**RoInspectCapturedStackBackTrace**](/windows/win32/api/roerrorapi/nf-roerrorapi-roinspectcapturedstackbacktrace) | Provides a way to for debuggers to inspect a call stack from a target process. |
| [**RoOriginateError**](/windows/win32/api/roerrorapi/nf-roerrorapi-rooriginateerror) | Reports an error and an informative string to an attached debugger. |
| [**RoOriginateErrorW**](/windows/win32/api/roerrorapi/nf-roerrorapi-rooriginateerrorw) | Reports an error and an informative string to an attached debugger. |
| [**RoOriginateLanguageException**](/windows/win32/api/roerrorapi/nf-roerrorapi-rooriginatelanguageexception) | Reports an error, an informative string, and an error object to an attached debugger. |
| [**RoParameterizedTypeExtraGetTypeSignature**](/windows/win32/api/roparameterizediid/nf-roparameterizediid-roparameterizedtypeextragettypesignature) | Gets the type signature used to compute the IID from the last call to [**RoGetParameterizedTypeInstanceIID**](/windows/win32/api/roparameterizediid/nf-roparameterizediid-rogetparameterizedtypeinstanceiid) with the specified handle. |
| [**RoParseTypeName**](/windows/win32/api/rometadataresolution/nf-rometadataresolution-roparsetypename) | Parses a type name and existing type parameters, in the case of parameterized types. |
| [**RoRegisterActivationFactories**](/windows/win32/api/roapi/nf-roapi-roregisteractivationfactories) | Registers an array out-of-process activation factories for a Windows Runtime exe server. |
| [**RoRegisterForApartmentShutdown**](/windows/win32/api/roapi/nf-roapi-roregisterforapartmentshutdown) | Registers an [**IApartmentShutdown**](/windows/desktop/api/objidl/nn-objidl-iapartmentshutdown) callback to be invoked when the current apartment shuts down. |
| [**RoReportUnhandledError**](/windows/win32/api/roerrorapi/nf-roerrorapi-roreportunhandlederror) | Triggers the Global Error Handler when an unhandled exception occurs. |
| [**RoReportFailedDelegate**](/windows/win32/api/roerrorapi/nf-roerrorapi-roreportfaileddelegate) | Triggers the Global Error Handler when a delegate failure occurs. |
| [**RoResolveNamespace**](/windows/win32/api/rometadataresolution/nf-rometadataresolution-roresolvenamespace) | Determine the direct children, types, and sub-namespaces of the specified Windows Runtime namespace, from any programming language supported by the Windows Runtime. |
| [**RoResolveRestrictedErrorInfoReference**](/windows/win32/api/roerrorapi/nf-roerrorapi-roresolverestrictederrorinforeference) | Returns the [**IRestrictedErrorInfo**](/windows/desktop/api/RestrictedErrorInfo/nn-restrictederrorinfo-irestrictederrorinfo) interface pointer based on the given reference. |
| [**RoRevokeActivationFactories**](/windows/win32/api/roapi/nf-roapi-rorevokeactivationfactories) | Removes an array of registered activation factories from the Windows Runtime. |
| [**RoSetErrorReportingFlags**](/windows/win32/api/roerrorapi/nf-roerrorapi-roseterrorreportingflags) | Sets the reporting behavior of Windows Runtime error functions. |
| [**RoTransformError**](/windows/win32/api/roerrorapi/nf-roerrorapi-rotransformerror) | Reports a modified error and an informative string to an attached debugger. |
| [**RoTransformErrorW**](/windows/win32/api/roerrorapi/nf-roerrorapi-rotransformerrorw) | Reports a transformed error and an informative string to an attached debugger. |
| [**RoUninitialize**](/windows/win32/api/roapi/nf-roapi-rouninitialize) | Closes the Windows Runtime on the current thread. |
| [**RoUnregisterForApartmentShutdown**](/windows/win32/api/roapi/nf-roapi-rounregisterforapartmentshutdown) | Unregisters a previously registered [**IApartmentShutdown**](/windows/desktop/api/objidl/nn-objidl-iapartmentshutdown) interface. |
| [**SetRestrictedErrorInfo**](/windows/win32/api/roerrorapi/nf-roerrorapi-setrestrictederrorinfo) | Sets the restricted error information object for the current thread. |
| [**WindowsCompareStringOrdinal**](/windows/win32/api/winstring/nf-winstring-windowscomparestringordinal) | Compares two specified [**HSTRING**](hstring.md) objects and returns an integer that indicates their relative position in a sort order. |
| [**WindowsConcatString**](/windows/win32/api/winstring/nf-winstring-windowsconcatstring) | Concatenates two specified strings. |
| [**WindowsCreateString**](/windows/win32/api/winstring/nf-winstring-windowscreatestring) | Creates a new [**HSTRING**](hstring.md) based on the specified source string. |
| [**WindowsCreateStringReference**](/windows/win32/api/winstring/nf-winstring-windowscreatestringreference) | Creates a new string reference based on the specified string. |
| [**WindowsDeleteString**](/windows/win32/api/winstring/nf-winstring-windowsdeletestring) | Decrements the reference count of a string buffer. |
| [**WindowsDeleteStringBuffer**](/windows/win32/api/winstring/nf-winstring-windowsdeletestringbuffer) | Discards a preallocated string buffer if it was not promoted to an [**HSTRING**](hstring.md). |
| [**WindowsDuplicateString**](/windows/win32/api/winstring/nf-winstring-windowsduplicatestring) | Creates a copy of the specified string. |
| [**WindowsGetStringLen**](/windows/win32/api/winstring/nf-winstring-windowsgetstringlen) | Gets the length, in Unicode characters, of the specified string. |
| [**WindowsGetStringRawBuffer**](/windows/win32/api/winstring/nf-winstring-windowsgetstringrawbuffer) | Gets the backing buffer for the specified string. |
| [**WindowsInspectString**](/windows/win32/api/winstring/nf-winstring-windowsinspectstring) | Provides a way to for debuggers to display the value of an Windows Runtime [**HSTRING**](hstring.md) in another address space, remotely, or from a dump.  |
| [**WindowsInspectString2**](/windows/win32/api/winstring/nf-winstring-windowsinspectstring2) | Provides a way to for debuggers to display the value of an Windows Runtime [**HSTRING**](hstring.md) in another address space, remotely, or from a dump.  |
| [**WindowsIsStringEmpty**](/windows/win32/api/winstring/nf-winstring-windowsisstringempty) | Indicates whether the specified string is the empty string. |
| [**WindowsPreallocateStringBuffer**](/windows/win32/api/winstring/nf-winstring-windowspreallocatestringbuffer) | Allocates a mutable character buffer for use in [**HSTRING**](hstring.md) creation. |
| [**WindowsPromoteStringBuffer**](/windows/win32/api/winstring/nf-winstring-windowspromotestringbuffer) | Creates an [**HSTRING**](hstring.md) from the specified [**HSTRING\_BUFFER**](hstring-buffer.md). |
| [**WindowsReplaceString**](/windows/win32/api/winstring/nf-winstring-windowsreplacestring) | Replaces all occurrences of a set of characters in the specified string with another set of characters to create a new string. |
| [**WindowsStringHasEmbeddedNull**](/windows/win32/api/winstring/nf-winstring-windowsstringhasembeddednull) | Indicates whether the specified string has embedded null characters. |
| [**WindowsSubstring**](/windows/win32/api/winstring/nf-winstring-windowssubstring) | Retrieves a substring from the specified string. The substring starts at the specified character position. |
| [**WindowsSubstringWithSpecifiedLength**](/windows/win32/api/winstring/nf-winstring-windowssubstringwithspecifiedlength) | Retrieves a substring from the specified string. The substring starts at a specified character position and has a specified length. |
| [**WindowsTrimStringEnd**](/windows/win32/api/winstring/nf-winstring-windowstrimstringend) | Removes all trailing occurrences of a specified set of characters from the source string. |
| [**WindowsTrimStringStart**](/windows/win32/api/winstring/nf-winstring-windowstrimstringstart) | Removes all leading occurrences of a specified set of characters from the source string. |



 

 

 
