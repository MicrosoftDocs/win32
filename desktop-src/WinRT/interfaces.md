---
description: Interfaces (Windows Runtime C++)
ms.assetid: CB05B5F8-BE15-4BE0-A651-F6E8912D649D
title: Interfaces (Windows Runtime)
ms.topic: article
ms.date: 05/31/2018
---

# Interfaces

## In this section

| Interface | Description |
|-|-|
| [**IActivatableClassRegistration**](/windows/win32/api/activationregistration/nn-activationregistration-iactivatableclassregistration) | Enables getting the registration info for a class. |
| [**IActivationFactory**](/windows/win32/api/activation/nn-activation-iactivationfactory) | Enables classes to be activated by the Windows Runtime. |
| [**IAgileReference**](/windows/desktop/api/objidl/nn-objidl-iagilereference) | Enables retrieving an agile reference to an object. |
| [**IApartmentShutdown**](/windows/desktop/api/objidl/nn-objidl-iapartmentshutdown) | Enables registration of an apartment shutdown notification handler. |
| [**AsyncActionCompletedHandler**](asyncactioncompletedhandler.md) | Represents the method that is called when an asynchronous action completes. |
| [**IAsyncAction**](/windows/win32/api/windows.foundation/nn-windows-foundation-iasyncaction) | Represents an asynchronous action. |
| [**IAsyncActionProgressHandler&lt;TProgress&gt;**](/previous-versions//br205782(v=vs.85)) | Represents the method that is called when an asynchronous action reports progress. |
| [**IAsyncActionWithProgress&lt;TProgress&gt;**](/previous-versions//br205784(v=vs.85)) | Represents an asynchronous action that reports progress. |
| [**IAsyncActionWithProgressCompletedHandler&lt;TProgress&gt;**](/previous-versions//br205785(v=vs.85)) | Represents the method that is called when an asynchronous action that reports progress completes. |
| [**IAsyncInfo**](/windows/win32/api/asyncinfo/nn-asyncinfo-iasyncinfo) | Provides support for asynchronous operations. |
| [**IAsyncOperation&lt;TResult&gt;**](/previous-versions//br205802(v=vs.85)) | Represents an asynchronous operation that returns a result. |
| [**IAsyncOperationCompletedHandler&lt;TResult&gt;**](/previous-versions//br205803(v=vs.85)) | Represents the method that is called when an asynchronous operation completes. |
| [**IAsyncOperationProgressHandler**](/previous-versions//br205805(v=vs.85)) | Represents the method that is called when an asynchronous operation reports progress. |
| [**IAsyncOperationWithProgress**](/previous-versions//br205807(v=vs.85)) | Represents an asynchronous operation that returns a result and reports progress. |
| [**IAsyncOperationWithProgressCompletedHandler<TResult, TProgress>**](/previous-versions//br205808(v=vs.85)) | Represents the method that is called when an asynchronous operation that reports progress completes. |
| [**IAudioFrameNative**](/windows/desktop/api/windows.media.core.interop/nn-windows-media-core-interop-iaudioframenative) | Represents a frame of audio data. |
| [**IAudioFrameNativeFactory**](/windows/desktop/api/windows.media.core.interop/nn-windows-media-core-interop-iaudioframenativefactory) | Creates instances of [**IAudioFrameNative**](/windows/desktop/api/windows.media.core.interop/nn-windows-media-core-interop-iaudioframenative). |
| [**IBuffer**](/previous-versions//hh438362(v=vs.85)) | Represents an array of bytes. |
| [**IBufferByteAccess**](/previous-versions//hh846267(v=vs.85)) | Represents a buffer as an array of bytes. |
| [**IClosable**](/windows/win32/api/windows.foundation/nn-windows-foundation-iclosable) | Defines a method to release allocated resources. |
| [**ICompositionDrawingSurfaceInterop**](/windows/win32/api/windows.ui.composition.interop/nn-windows-ui-composition-interop-icompositiondrawingsurfaceinterop) | Native interoperation interface that allows drawing on a surface object using a RECT to define the area to draw into. |
| [**ICompositionDrawingSurfaceInterop2**](/windows/win32/api/windows.ui.composition.interop/nn-windows-ui-composition-interop-icompositiondrawingsurfaceinterop2) | A native interoperation interface that allows you to read back the contents of a composition drawing surface (or a composition virtual drawing surface). |
| [**ICompositionGraphicsDeviceInterop**](/windows/win32/api/windows.ui.composition.interop/nn-windows-ui-composition-interop-icompositiongraphicsdeviceinterop) | A native interoperation interface that allows getting and setting the graphics device. |
| [**IContactManagerInterop**](/previous-versions//dn302109(v=vs.85)) | Enables access to [**ContactManager**](/uwp/api/Windows.ApplicationModel.Contacts.ContactManager?view=winrt-19041) methods in an app that manages multiple windows. |
| [**ICoreApplication**](/previous-versions//hh438365(v=vs.85)) | Enables apps to handle state changes, manage windows, and integrate with a variety of UI frameworks. |
| [**ICoreApplicationExit**](/previous-versions//hh438366(v=vs.85)) | Provides the means for Windows Store apps to stop running. |
| [**ICoreApplicationInitialization**](/previous-versions//hh438370(v=vs.85)) | Contains a run method that is used to start the application object from the entry point of an app. |
| [**ICoreApplicationView**](/previous-versions//hh438372(v=vs.85)) | Represents a view of an application. |
| [**ICoreImmersiveApplication**](/previous-versions//hh438382(v=vs.85)) | Contains methods for managing views in an app. |
| [**ICoreInputInterop**](/windows/desktop/api/corewindow/nn-corewindow-icoreinputinterop) | Enables an input source on a Windows Store app's [**CoreInput**](https://www.bing.com/search?q=**CoreInput**) object. |
| [**ICoreWindowInterop**](/windows/desktop/api/corewindow/nn-corewindow-icorewindowinterop) | Enables apps to obtain the window handleof the window ([**CoreWindow**](/uwp/api/Windows.UI.Core.CoreWindow?view=winrt-19041)) associated with this interface. |
| [**IDllServerActivatableClassRegistration**](/windows/win32/api/activationregistration/nn-activationregistration-idllserveractivatableclassregistration) | Enables getting the registration info for an in-process server. |
| [**IErrorReportingSettings**](/previous-versions//br205818(v=vs.85)) | Provides debugger integration for Windows Runtime applications. |
| [**IEventHandler&lt;T&gt;**](/previous-versions//hh438385(v=vs.85)) | Represents the method that will handle an event that has event data of type **T**. |
| [**IExeServerActivatableClassRegistration**](/windows/win32/api/activationregistration/nn-activationregistration-iexeserveractivatableclassregistration) | Enables getting the registration info for an out-of-process server. |
| [**IExeServerRegistration**](/windows/win32/api/activationregistration/nn-activationregistration-iexeserverregistration) | Represents a registered an out-of-process server. |
| [**IFindReferenceTargetsCallback**](/windows/win32/api/windows.ui.xaml.hosting.referencetracker/nn-windows-ui-xaml-hosting-referencetracker-ifindreferencetargetscallback) | Defines the interface for callbacks from [**IReferenceTracker::FindTrackerTargets**](/windows/win32/api/windows.ui.xaml.hosting.referencetracker/nf-windows-ui-xaml-hosting-referencetracker-ireferencetracker-findtrackertargets). The implementation of this interface must pass any [**IReferenceTrackerTarget**](/windows/win32/api/windows.ui.xaml.hosting.referencetracker/nn-windows-ui-xaml-hosting-referencetracker-ireferencetrackertarget) instances it finds to the **FoundTrackerTarget** method. |
| [**IInputPaneInterop**](/windows/desktop/api/inputpaneinterop/nn-inputpaneinterop-iinputpaneinterop) | Enables access to the members of the [**InputPane**](/uwp/api/Windows.UI.ViewManagement.InputPane?view=winrt-19041) class in a desktop app. |
| [**IInputStream**](/previous-versions//hh438387(v=vs.85)) | Enables obtaining an asynchronous reader operation on a sequential stream of bytes. |
| [**IInspectable**](/windows/win32/api/inspectable/nn-inspectable-iinspectable) | Provides functionality required for all Windows Runtime classes. |
| [**IIterable&lt;T&gt;**](/previous-versions//br205825(v=vs.85)) | Exposes the iterator, which supports simple iteration over a collection of a specified type. |
| [**IIterator&lt;T&gt;**](/previous-versions//br205827(v=vs.85)) | Supports iteration over a collection. |
| [**IKeyValuePair<K, V>**](/previous-versions//br205831(v=vs.85)) | Represents a key-value pair. |
| [**ILanguageExceptionErrorInfo**](/windows/desktop/api/restrictederrorinfo/nn-restrictederrorinfo-ilanguageexceptionerrorinfo) | Enables retrieving the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) pointer stored in the error info with the call to RoOriginateLanguageException. |
| [**ILanguageExceptionErrorInfo2**](/windows/desktop/api/restrictederrorinfo/nn-restrictederrorinfo-ilanguageexceptionerrorinfo2) | Enables language projections to provide and retrieve error information as with [**ILanguageExceptionErrorInfo**](/windows/desktop/api/restrictederrorinfo/nn-restrictederrorinfo-ilanguageexceptionerrorinfo), with the additional benefit of working across language boundaries. |
| [**ILanguageExceptionTransform**](/windows/desktop/api/restrictederrorinfo/nn-restrictederrorinfo-ilanguageexceptiontransform) | Allows language projections to make available to the system any and all context from an exception that gets thrown from the context of a catch handler that catches a different exception. |
| [**ILanguageExceptionStackBackTrace**](/windows/desktop/api/restrictederrorinfo/nn-restrictederrorinfo-ilanguageexceptionstackbacktrace) | Allows projections to provide custom stack trace for that exception. |
| [**IMap<K, V>**](/previous-versions//br205834(v=vs.85)) | Represents an associative collection. |
| [**IMapChangedEventArgs&lt;K&gt;**](/previous-versions//br205835(v=vs.85)) | Provides data for a [**MapChanged**](/uwp/api/windows.foundation.collections.iobservablemap-2?view=winrt-19041) event. |
| [**IMapView<K, V>**](/previous-versions//br205838(v=vs.85)) | Represents an immutable view into a [**IMap(K,V)**](/previous-versions//br205834(v=vs.85)). |
| [**IMemoryBufferByteAccess**](/previous-versions//mt297505(v=vs.85)) | Provides access to an [**IMemoryBuffer**](/uwp/api/Windows.Foundation.IMemoryBuffer?view=winrt-19041) as an array of bytes. |
| [**IMetaDataAssemblyImport**](/windows/win32/api/rometadataapi/nn-rometadataapi-imetadataassemblyimport) | Provides methods to access and examine the contents of an assembly manifest. |
| [**IMetaDataDispenser**](/windows/win32/api/rometadataapi/nn-rometadataapi-imetadatadispenser) | Provides methods to create a new metadata scope, or open an existing one. |
| [**IMetaDataDispenserEx**](/windows/win32/api/rometadataapi/nn-rometadataapi-imetadatadispenserex) | Extends the [**IMetaDataDispenser**](/windows/win32/api/rometadataapi/nn-rometadataapi-imetadatadispenser) interface to provide the capability to control how the metadata APIs operate on the current metadata scope. |
| [**IMetaDataImport**](/windows/win32/api/rometadataapi/nn-rometadataapi-imetadataimport) | Provides methods for importing and manipulating existing metadata from a portable executable (PE) file or other source, such as a type library or a stand-alone, run-time metadata binary. |
| [**IMetaDataImport2**](/windows/win32/api/rometadataapi/nn-rometadataapi-imetadataimport2) | Extends the [**IMetaDataImport**](/windows/win32/api/rometadataapi/nn-rometadataapi-imetadataimport) interface to provide the capability of working with generic types. |
| [**IMetaDataTables**](/windows/win32/api/rometadataapi/nn-rometadataapi-imetadatatables) | Provides methods for the storage and retrieval of metadata information in tables. |
| [**IMetaDataTables2**](/windows/win32/api/rometadataapi/nn-rometadataapi-imetadatatables2) | Extends [**IMetaDataTables**](/windows/win32/api/rometadataapi/nn-rometadataapi-imetadatatables) to include methods for working with metadata streams. |
| [**IObservableMap<K, V>**](/previous-versions//br205851(v=vs.85)) | Notifies event handlers of dynamic changes to a map, such as when items get added or removed. |
| [**IObservableVector&lt;T&gt;**](/previous-versions//br205854(v=vs.85)) | Notifies event handlers of changes to the vector. |
| [**IOplockBreakingHandler**](/windows/desktop/api/windowsstoragecom/nn-windowsstoragecom-ioplockbreakinghandler) | This interface is not currently implemented. |
| [**IOutputStream**](/previous-versions//hh438390(v=vs.85)) | Enables obtaining an asynchronous writer operation on a sequential stream of bytes. |
| [**IPdfRendererNative**](/windows/desktop/api/windows.data.pdf.interop/nn-windows-data-pdf-interop-ipdfrenderernative) | Represents a high-performance API for displaying a single page of a Portable Document Format (PDF) file. |
| [**IPackageDebugSettings**](/previous-versions//hh438393(v=vs.85)) | Enables debugger developers control over the lifecycle of a Windows Store app, such as when it is suspended or resumed. |
| [**IPlayToManagerInterop**](/windows/desktop/api/playtomanagerinterop/nn-playtomanagerinterop-iplaytomanagerinterop) | Enables access to [**PlayToManager**](/uwp/api/Windows.Media.PlayTo.PlayToManager?view=winrt-19041) methods in a Windows Store app that manages multiple windows. |
| [**IPrintManagerInterop**](/windows/desktop/api/printmanagerinterop/nn-printmanagerinterop-iprintmanagerinterop) | Enables access to [**PrintManager**](/uwp/api/Windows.Graphics.Printing.PrintManager?view=winrt-19041) methods in a Windows Store app that manages multiple windows. |
| [**IPropertyValue**](/windows/win32/api/windows.foundation/nn-windows-foundation-ipropertyvalue) | Represents a value in a Windows Runtime property store. |
| [**IPropertyValueStatics**](/windows/win32/api/windows.foundation/nn-windows-foundation-ipropertyvaluestatics) | Creates [**IPropertyValue**](/windows/win32/api/windows.foundation/nn-windows-foundation-ipropertyvalue) objects that you can store in a property store. |
| [**IRandomAccessStream**](/previous-versions//hh438400(v=vs.85)) | Enables obtaining an asynchronous byte reader or byte writer that's positioned at the specified location on a random access byte stream. |
| [**IRandomAccessStreamFileAccessMode**](/windows/desktop/api/windowsstoragecom/nn-windowsstoragecom-irandomaccessstreamfileaccessmode) | Provides access to the file access mode that was used when the [**StorageFile.OpenAsync**](/uwp/api/Windows.Storage.StorageFile?view=winrt-19041) method was called to open the random-access byte stream. |
| [**IReference&lt;T&gt;**](/previous-versions//br224583(v=vs.85)) | Enables extending the Windows Runtime property system for user-defined enumerations, structures, and delegate types. |
| [**IReferenceArray&lt;T&gt;**](/previous-versions//br224584(v=vs.85)) | Enables extending the Windows Runtime property system for arrays of user-defined enumerations, structures, and delegate types. |
| [**IReferenceTracker**](/windows/win32/api/windows.ui.xaml.hosting.referencetracker/nn-windows-ui-xaml-hosting-referencetracker-ireferencetracker) | Defines the interface implemented by the XAML framework for managing XAML object references. |
| [**IReferenceTrackerHost**](/windows/win32/api/windows.ui.xaml.hosting.referencetracker/nn-windows-ui-xaml-hosting-referencetracker-ireferencetrackerhost) | Defines an interface that provides the global services used by the garbage collection (GC) system used by the XAML framework. |
| [**IReferenceTrackerManager**](/windows/win32/api/windows.ui.xaml.hosting.referencetracker/nn-windows-ui-xaml-hosting-referencetracker-ireferencetrackermanager) | Defines the interface for a XAML object reference manager. Implement this interface to manage instances of [**IReferenceTracker**](/windows/win32/api/windows.ui.xaml.hosting.referencetracker/nn-windows-ui-xaml-hosting-referencetracker-ireferencetracker) on XAML objects. |
| [**IReferenceTrackerTarget**](/windows/win32/api/windows.ui.xaml.hosting.referencetracker/nn-windows-ui-xaml-hosting-referencetracker-ireferencetrackertarget) | Defines an interface implemented by a garbage collector object referenced from XAML. |
| [**IRestrictedErrorInfo**](/windows/desktop/api/RestrictedErrorInfo/nn-restrictederrorinfo-irestrictederrorinfo) | Represents the details of an error, including restricted error information. |
| [**ISoftwareBitmapNative**](/windows/desktop/api/windows.graphics.imaging.interop/nn-windows-graphics-imaging-interop-isoftwarebitmapnative) | Represents a software bitmap. |
| [**ISoftwareBitmapNativeFactory**](/windows/desktop/api/windows.graphics.imaging.interop/nn-windows-graphics-imaging-interop-isoftwarebitmapnativefactory) | Creates instances of [**ISoftwareBitmapNative**](/windows/desktop/api/windows.graphics.imaging.interop/nn-windows-graphics-imaging-interop-isoftwarebitmapnative). |
| [**IStorageFolderHandleAccess**](/windows/desktop/api/windowsstoragecom/nn-windowsstoragecom-istoragefolderhandleaccess) | Provides access to the operating system handle of a storage folder. |
| [**IStorageItemHandleAccess**](/windows/desktop/api/windowsstoragecom/nn-windowsstoragecom-istorageitemhandleaccess) | Provides access to the operating system handle of a storage file. |
| [**IStringable**](/windows/win32/api/windows.foundation/nn-windows-foundation-istringable) | Provides a way to represent the current object as a string. |
| [**ISurfaceImageSourceManagerNative**](/windows/desktop/api/windows.ui.xaml.media.dxinterop/nn-windows-ui-xaml-media-dxinterop-isurfaceimagesourcemanagernative) | Enables performing bulk operations across all [**SurfaceImageSource**](/uwp/api/Windows.UI.Xaml.Media.Imaging.SurfaceImageSource?view=winrt-19041) objects created in the same process. |
| [**ISurfaceImageSourceNativeWithD2D**](/windows/desktop/api/windows.ui.xaml.media.dxinterop/nn-windows-ui-xaml-media-dxinterop-isurfaceimagesourcenativewithd2d) | Provides the implementation of a shared Microsoft DirectX surface which is displayed in a [**SurfaceImageSource**](/uwp/api/Windows.UI.Xaml.Media.Imaging.SurfaceImageSource?view=winrt-19041) or [**VirtualSurfaceImageSource**](/uwp/api/Windows.UI.Xaml.Media.Imaging.VirtualSurfaceImageSource?view=winrt-19041). |
| [**ISurfaceImageSourceNative**](/windows/desktop/api/windows.ui.xaml.media.dxinterop/nn-windows-ui-xaml-media-dxinterop-isurfaceimagesourcenative) | Provides the implementation of a shared fixed-size surface for Direct2D drawing. |
| [**ISuspendingDeferral**](isuspendingdeferral.md) | Manages a delayed app suspending operation. |
| [**ISuspendingEventArgs**](isuspendingeventargs.md) | Provides data for an app suspending event. |
| [**ISuspendingOperation**](isuspendingoperation.md) | Provides information about an app suspending operation. |
| [**ISwapChainBackgroundPanelNative**](/windows/desktop/api/windows.ui.xaml.media.dxinterop/nn-windows-ui-xaml-media-dxinterop-iswapchainbackgroundpanelnative) | Provides interoperation between XAML and a DirectX swap chain. |
| [**ISwapChainPanelNative**](/windows/desktop/api/windows.ui.xaml.media.dxinterop/nn-windows-ui-xaml-media-dxinterop-iswapchainpanelnative) | Provides interoperation between XAML and a DirectX swap chain. Unlike [**SwapChainBackgroundPanel**](/uwp/api/Windows.UI.Xaml.Controls.SwapChainBackgroundPanel?view=winrt-19041), a **SwapChainPanel** can appear at any level in the XAML display tree, and more than 1 can be present in any given tree. |
| [**ISwapChainPanelNative2**](/windows/desktop/api/windows.ui.xaml.media.dxinterop/nn-windows-ui-xaml-media-dxinterop-iswapchainpanelnative2) | Provides interoperation between XAML and a DirectX swap chain. Unlike [**SwapChainBackgroundPanel**](/uwp/api/Windows.UI.Xaml.Controls.SwapChainBackgroundPanel?view=winrt-19041), a **SwapChainPanel** can appear at any level in the XAML display tree, and more than 1 can be present in any given tree. |
| [**ITypedEventHandler<TSender, TArgs>**](/previous-versions//hh438424(v=vs.85)) | Represents the method that will handle an event from a sender of type **TSender** and event data of type **T**. |
| [**IUnbufferedFileHandleOplockCallback**](/windows/desktop/api/windowsstoragecom/nn-windowsstoragecom-iunbufferedfilehandleoplockcallback) | Defines a callback method that you want to run when the opportunistic lock for a handle that you get by calling the [**IUnbufferedFileHandleProvider::OpenUnbufferedFileHandle**](/windows/desktop/api/windowsstoragecom/nf-windowsstoragecom-iunbufferedfilehandleprovider-openunbufferedfilehandle) method is broken. |
| [**IUnbufferedFileHandleProvider**](/windows/desktop/api/windowsstoragecom/nn-windowsstoragecom-iunbufferedfilehandleprovider) | Provides access to handles from a random-access byte stream that the [**StorageFile.OpenAsync**](/uwp/api/Windows.Storage.StorageFile?view=winrt-19041) method created. |
| [**IVector&lt;T&gt;**](/previous-versions//br224590(v=vs.85)) | Represents a random-access collection of elements. |
| [**IVectorChangedEventArgs**](ivectorchangedeventargs.md) | Provides data for a [**VectorChanged**](/uwp/api/windows.foundation.collections.iobservablevector-1?view=winrt-19041) event. |
| [**IVectorView&lt;T&gt;**](/previous-versions//br224594(v=vs.85)) | Represents an immutable view into a [**IVector(T)**](/uwp/api/windows.foundation.collections.ivector-1?view=winrt-19041). |
| [**IVideoFrameNative**](/windows/desktop/api/windows.media.core.interop/nn-windows-media-core-interop-ivideoframenative) | Represents a frame of video data. |
| [**IVideoFrameNativeFactory**](/windows/desktop/api/windows.media.core.interop/nn-windows-media-core-interop-ivideoframenativefactory) | Creates instances of [**IVideoFrameNative**](/windows/desktop/api/windows.media.core.interop/nn-windows-media-core-interop-ivideoframenative). |
| [**IViewProvider**](/previous-versions//hh438426(v=vs.85)) | Represents a view in an application. |
| [**IViewProviderFactory**](/previous-versions//hh438427(v=vs.85)) | Creates an instance of views that implement the [**IViewProvider**](/previous-versions//hh438426(v=vs.85)) interface. |
| [**IVirtualSurfaceImageSourceNative**](/windows/desktop/api/windows.ui.xaml.media.dxinterop/nn-windows-ui-xaml-media-dxinterop-ivirtualsurfaceimagesourcenative) | Provides the implementation of a large (greater than the screen size) shared surface for DirectX drawing. |
| [**IVirtualSurfaceUpdatesCallbackNative**](/windows/desktop/api/windows.ui.xaml.media.dxinterop/nn-windows-ui-xaml-media-dxinterop-ivirtualsurfaceupdatescallbacknative) | Provides an interface for the implementation of drawing behaviors when a [**VirtualSurfaceImageSource**](/windows/desktop/api/windows.ui.xaml.media.dxinterop/nn-windows-ui-xaml-media-dxinterop-ivirtualsurfaceimagesourcenative) requests an update. |
| [**IWeakReference**](/windows/win32/api/weakreference/nn-weakreference-iweakreference) | Represents a weak reference to an object. |
| [**IWeakReferenceSource**](/windows/win32/api/weakreference/nn-weakreference-iweakreferencesource) | Represents a source object to which a weak reference can be retrieved. |
| [**MapChangedEventHandler<K, V>**](/previous-versions//br224612(v=vs.85)) | Represents the method that handles the [**MapChanged**](/uwp/api/windows.foundation.collections.iobservablemap-2?view=winrt-19041) event of an observable map. |
| [**VectorChangedEventHandler&lt;T&gt;**](/previous-versions//br224626(v=vs.85)) | Represents the method that handles the [**VectorChanged**](/uwp/api/windows.foundation.collections.iobservablevector-1?view=winrt-19041) event of an observable vector. |
