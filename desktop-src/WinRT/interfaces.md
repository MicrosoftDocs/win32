---
Description: Interfaces (Windows Runtime C++)
ms.assetid: CB05B5F8-BE15-4BE0-A651-F6E8912D649D
title: Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Interfaces

## In this section

| Interface | Description |
|-|-|
| [**IActivatableClassRegistration**](https://msdn.microsoft.com/library/Dn408448(v=VS.85).aspx) | Enables getting the registration info for a class. |
| [**IActivationFactory**](https://msdn.microsoft.com/library/BR205779(v=VS.85).aspx) | Enables classes to be activated by the Windows Runtime. |
| [**IAgileReference**](/windows/desktop/api/objidl/nn-objidl-iagilereference) | Enables retrieving an agile reference to an object. |
| [**IApartmentShutdown**](/windows/desktop/api/objidl/nn-objidl-iapartmentshutdown) | Enables registration of an apartment shutdown notification handler. |
| [**AsyncActionCompletedHandler**](asyncactioncompletedhandler.md) | Represents the method that is called when an asynchronous action completes. |
| [**IAsyncAction**](https://msdn.microsoft.com/library/BR205781(v=VS.85).aspx) | Represents an asynchronous action. |
| [**IAsyncActionProgressHandler<TProgress>**](https://msdn.microsoft.com/library/BR205782(v=VS.85).aspx) | Represents the method that is called when an asynchronous action reports progress. |
| [**IAsyncActionWithProgress<TProgress>**](https://msdn.microsoft.com/library/BR205784(v=VS.85).aspx) | Represents an asynchronous action that reports progress. |
| [**IAsyncActionWithProgressCompletedHandler<TProgress>**](https://msdn.microsoft.com/library/BR205785(v=VS.85).aspx) | Represents the method that is called when an asynchronous action that reports progress completes. |
| [**IAsyncInfo**](https://msdn.microsoft.com/library/BR205795(v=VS.85).aspx) | Provides support for asynchronous operations. |
| [**IAsyncOperation<TResult>**](https://msdn.microsoft.com/library/BR205802(v=VS.85).aspx) | Represents an asynchronous operation that returns a result. |
| [**IAsyncOperationCompletedHandler<TResult>**](https://msdn.microsoft.com/library/BR205803(v=VS.85).aspx) | Represents the method that is called when an asynchronous operation completes. |
| [**IAsyncOperationProgressHandler**](https://msdn.microsoft.com/library/BR205805(v=VS.85).aspx) | Represents the method that is called when an asynchronous operation reports progress. |
| [**IAsyncOperationWithProgress**](https://msdn.microsoft.com/library/BR205807(v=VS.85).aspx) | Represents an asynchronous operation that returns a result and reports progress. |
| [**IAsyncOperationWithProgressCompletedHandler<TResult, TProgress>**](https://msdn.microsoft.com/library/BR205808(v=VS.85).aspx) | Represents the method that is called when an asynchronous operation that reports progress completes. |
| [**IAudioFrameNative**](/windows/desktop/api/windows.media.core.interop/nn-windows-media-core-interop-iaudioframenative) | Represents a frame of audio data. |
| [**IAudioFrameNativeFactory**](/windows/desktop/api/windows.media.core.interop/nn-windows-media-core-interop-iaudioframenativefactory) | Creates instances of [**IAudioFrameNative**](/windows/desktop/api/windows.media.core.interop/nn-windows-media-core-interop-iaudioframenative). |
| [**IBuffer**](https://msdn.microsoft.com/library/Hh438362(v=VS.85).aspx) | Represents an array of bytes. |
| [**IBufferByteAccess**](https://msdn.microsoft.com/library/Hh846267(v=VS.85).aspx) | Represents a buffer as an array of bytes. |
| [**IClosable**](https://msdn.microsoft.com/library/Hh846269(v=VS.85).aspx) | Defines a method to release allocated resources. |
| [**ICompositionDrawingSurfaceInterop**](/windows/win32/api/windows.ui.composition.interop/nn-windows-ui-composition-interop-icompositiondrawingsurfaceinterop) | Native interoperation interface that allows drawing on a surface object using a RECT to define the area to draw into. |
| [**ICompositionDrawingSurfaceInterop2**](/windows/win32/windows.ui.composition.interop/windows.ui.composition.interop/nn-windows-ui-composition-interop-icompositiondrawingsurfaceinterop2) | A native interoperation interface that allows you to read back the contents of a composition drawing surface (or a composition virtual drawing surface). |
| [**ICompositionGraphicsDeviceInterop**](/windows/win32/api/windows.ui.composition.interop/nn-windows-ui-composition-interop-icompositiongraphicsdeviceinterop) | A native interoperation interface that allows getting and setting the graphics device. |
| [**IContactManagerInterop**](https://msdn.microsoft.com/library/Dn302109(v=VS.85).aspx) | Enables access to [**ContactManager**](https://msdn.microsoft.com/library/Dn263564(v=WIN.10).aspx) methods in an app that manages multiple windows. |
| [**ICoreApplication**](https://msdn.microsoft.com/library/Hh438365(v=VS.85).aspx) | Enables apps to handle state changes, manage windows, and integrate with a variety of UI frameworks. |
| [**ICoreApplicationExit**](https://msdn.microsoft.com/library/Hh438366(v=VS.85).aspx) | Provides the means for Windows Store apps to stop running. |
| [**ICoreApplicationInitialization**](https://msdn.microsoft.com/library/Hh438370(v=VS.85).aspx) | Contains a run method that is used to start the application object from the entry point of an app. |
| [**ICoreApplicationView**](https://msdn.microsoft.com/library/Hh438372(v=VS.85).aspx) | Represents a view of an application. |
| [**ICoreImmersiveApplication**](https://msdn.microsoft.com/library/Hh438382(v=VS.85).aspx) | Contains methods for managing views in an app. |
| [**ICoreInputInterop**](/windows/desktop/api/corewindow/nn-corewindow-icoreinputinterop) | Enables an input source on a Windows Store app's [**CoreInput**](https://www.bing.com/search?q=**CoreInput**) object. |
| [**ICoreWindowInterop**](/windows/desktop/api/corewindow/nn-corewindow-icorewindowinterop) | Enables apps to obtain the window handleof the window ([**CoreWindow**](https://msdn.microsoft.com/library/BR208225(v=Win.10).aspx)) associated with this interface. |
| [**IDllServerActivatableClassRegistration**](https://msdn.microsoft.com/library/Dn408455(v=VS.85).aspx) | Enables getting the registration info for an in-process server. |
| [**IErrorReportingSettings**](https://msdn.microsoft.com/library/BR205818(v=VS.85).aspx) | Provides debugger integration for Windows Runtime applications. |
| [**IEventHandler<T>**](https://msdn.microsoft.com/library/Hh438385(v=VS.85).aspx) | Represents the method that will handle an event that has event data of type **T**. |
| [**IExeServerActivatableClassRegistration**](https://msdn.microsoft.com/library/Dn408458(v=VS.85).aspx) | Enables getting the registration info for an out-of-process server. |
| [**IExeServerRegistration**](https://msdn.microsoft.com/library/Dn408460(v=VS.85).aspx) | Represents a registered an out-of-process server. |
| [**IFindReferenceTargetsCallback**](https://msdn.microsoft.com/library/JJ542493(v=VS.85).aspx) | Defines the interface for callbacks from [**IReferenceTracker::FindTrackerTargets**](https://msdn.microsoft.com/library/JJ542516(v=VS.85).aspx). The implementation of this interface must pass any [**IReferenceTrackerTarget**](https://msdn.microsoft.com/library/JJ542508(v=VS.85).aspx) instances it finds to the **FoundTrackerTarget** method. |
| [**IInputPaneInterop**](/windows/desktop/api/inputpaneinterop/nn-inputpaneinterop-iinputpaneinterop) | Enables access to the members of the [**InputPane**](https://msdn.microsoft.com/library/BR242255(v=Win.10).aspx) class in a desktop app. |
| [**IInputStream**](https://msdn.microsoft.com/library/Hh438387(v=VS.85).aspx) | Enables obtaining an asynchronous reader operation on a sequential stream of bytes. |
| [**IInspectable**](https://msdn.microsoft.com/library/BR205821(v=VS.85).aspx) | Provides functionality required for all Windows Runtime classes. |
| [**IIterable<T>**](https://msdn.microsoft.com/library/BR205825(v=VS.85).aspx) | Exposes the iterator, which supports simple iteration over a collection of a specified type. |
| [**IIterator<T>**](https://msdn.microsoft.com/library/BR205827(v=VS.85).aspx) | Supports iteration over a collection. |
| [**IKeyValuePair<K, V>**](https://msdn.microsoft.com/library/BR205831(v=VS.85).aspx) | Represents a key-value pair. |
| [**ILanguageExceptionErrorInfo**](/windows/desktop/api/restrictederrorinfo/nn-restrictederrorinfo-ilanguageexceptionerrorinfo) | Enables retrieving the [**IUnknown**](https://msdn.microsoft.com/library/ms680509(v=VS.85).aspx) pointer stored in the error info with the call to RoOriginateLanguageException. |
| [**ILanguageExceptionErrorInfo2**](/windows/desktop/api/restrictederrorinfo/nn-restrictederrorinfo-ilanguageexceptionerrorinfo2) | Enables language projections to provide and retrieve error information as with [**ILanguageExceptionErrorInfo**](/windows/desktop/api/restrictederrorinfo/nn-restrictederrorinfo-ilanguageexceptionerrorinfo), with the additional benefit of working across language boundaries. |
| [**ILanguageExceptionTransform**](/windows/desktop/api/restrictederrorinfo/nn-restrictederrorinfo-ilanguageexceptiontransform) | Allows language projections to make available to the system any and all context from an exception that gets thrown from the context of a catch handler that catches a different exception. |
| [**ILanguageExceptionStackBackTrace**](/windows/desktop/api/restrictederrorinfo/nn-restrictederrorinfo-ilanguageexceptionstackbacktrace) | Allows projections to provide custom stack trace for that exception. |
| [**IMap<K, V>**](https://msdn.microsoft.com/library/BR205834(v=VS.85).aspx) | Represents an associative collection. |
| [**IMapChangedEventArgs<K>**](https://msdn.microsoft.com/library/BR205835(v=VS.85).aspx) | Provides data for a [**MapChanged**](https://msdn.microsoft.com/library/BR226051(v=Win.10).aspx) event. |
| [**IMapView<K, V>**](https://msdn.microsoft.com/library/BR205838(v=VS.85).aspx) | Represents an immutable view into a [**IMap(K,V)**](https://msdn.microsoft.com/library/BR205834(v=VS.85).aspx). |
| [**IMemoryBufferByteAccess**](https://msdn.microsoft.com/library/Mt297505(v=VS.85).aspx) | Provides access to an [**IMemoryBuffer**](https://msdn.microsoft.com/library/Dn921670(v=WIN.10).aspx) as an array of bytes. |
| [**IMetaDataAssemblyImport**](https://msdn.microsoft.com/library/Hh870550(v=VS.85).aspx) | Provides methods to access and examine the contents of an assembly manifest. |
| [**IMetaDataDispenser**](https://msdn.microsoft.com/library/Hh870566(v=VS.85).aspx) | Provides methods to create a new metadata scope, or open an existing one. |
| [**IMetaDataDispenserEx**](https://msdn.microsoft.com/library/Hh870567(v=VS.85).aspx) | Extends the [**IMetaDataDispenser**](https://msdn.microsoft.com/library/Hh870566(v=VS.85).aspx) interface to provide the capability to control how the metadata APIs operate on the current metadata scope. |
| [**IMetaDataImport**](https://msdn.microsoft.com/library/Hh870577(v=VS.85).aspx) | Provides methods for importing and manipulating existing metadata from a portable executable (PE) file or other source, such as a type library or a stand-alone, run-time metadata binary. |
| [**IMetaDataImport2**](https://msdn.microsoft.com/library/Hh870578(v=VS.85).aspx) | Extends the [**IMetaDataImport**](https://msdn.microsoft.com/library/Hh870577(v=VS.85).aspx) interface to provide the capability of working with generic types. |
| [**IMetaDataTables**](https://msdn.microsoft.com/library/Hh870643(v=VS.85).aspx) | Provides methods for the storage and retrieval of metadata information in tables. |
| [**IMetaDataTables2**](https://msdn.microsoft.com/library/Hh870644(v=VS.85).aspx) | Extends [**IMetaDataTables**](https://msdn.microsoft.com/library/Hh870643(v=VS.85).aspx) to include methods for working with metadata streams. |
| [**IObservableMap<K, V>**](https://msdn.microsoft.com/library/BR205851(v=VS.85).aspx) | Notifies event handlers of dynamic changes to a map, such as when items get added or removed. |
| [**IObservableVector<T>**](https://msdn.microsoft.com/library/BR205854(v=VS.85).aspx) | Notifies event handlers of changes to the vector. |
| [**IOplockBreakingHandler**](/windows/desktop/api/windowsstoragecom/nn-windowsstoragecom-ioplockbreakinghandler) | This interface is not currently implemented. |
| [**IOutputStream**](https://msdn.microsoft.com/library/Hh438390(v=VS.85).aspx) | Enables obtaining an asynchronous writer operation on a sequential stream of bytes. |
| [**IPdfRendererNative**](/windows/desktop/api/windows.data.pdf.interop/nn-windows-data-pdf-interop-ipdfrenderernative) | Represents a high-performance API for displaying a single page of a Portable Document Format (PDF) file. |
| [**IPackageDebugSettings**](https://msdn.microsoft.com/library/Hh438393(v=VS.85).aspx) | Enables debugger developers control over the lifecycle of a Windows Store app, such as when it is suspended or resumed. |
| [**IPlayToManagerInterop**](/windows/desktop/api/playtomanagerinterop/nn-playtomanagerinterop-iplaytomanagerinterop) | Enables access to [**PlayToManager**](https://msdn.microsoft.com/library/BR206972(v=Win.10).aspx) methods in a Windows Store app that manages multiple windows. |
| [**IPrintManagerInterop**](/windows/desktop/api/printmanagerinterop/nn-printmanagerinterop-iprintmanagerinterop) | Enables access to [**PrintManager**](https://msdn.microsoft.com/library/BR226426(v=Win.10).aspx) methods in a Windows Store app that manages multiple windows. |
| [**IPropertyValue**](https://msdn.microsoft.com/library/BR224510(v=VS.85).aspx) | Represents a value in a Windows Runtime property store. |
| [**IPropertyValueStatics**](https://msdn.microsoft.com/library/BR224511(v=VS.85).aspx) | Creates [**IPropertyValue**](https://msdn.microsoft.com/library/BR224510(v=VS.85).aspx) objects that you can store in a property store. |
| [**IRandomAccessStream**](https://msdn.microsoft.com/library/Hh438400(v=VS.85).aspx) | Enables obtaining an asynchronous byte reader or byte writer that's positioned at the specified location on a random access byte stream. |
| [**IRandomAccessStreamFileAccessMode**](/windows/desktop/api/windowsstoragecom/nn-windowsstoragecom-irandomaccessstreamfileaccessmode) | Provides access to the file access mode that was used when the [**StorageFile.OpenAsync**](https://msdn.microsoft.com/library/BR227221(v=Win.10).aspx) method was called to open the random-access byte stream. |
| [**IReference<T>**](https://msdn.microsoft.com/library/BR224583(v=VS.85).aspx) | Enables extending the Windows Runtime property system for user-defined enumerations, structures, and delegate types. |
| [**IReferenceArray<T>**](https://msdn.microsoft.com/library/BR224584(v=VS.85).aspx) | Enables extending the Windows Runtime property system for arrays of user-defined enumerations, structures, and delegate types. |
| [**IReferenceTracker**](https://msdn.microsoft.com/library/JJ542495(v=VS.85).aspx) | Defines the interface implemented by the XAML framework for managing XAML object references. |
| [**IReferenceTrackerHost**](https://msdn.microsoft.com/library/JJ542496(v=VS.85).aspx) | Defines an interface that provides the global services used by the garbage collection (GC) system used by the XAML framework. |
| [**IReferenceTrackerManager**](https://msdn.microsoft.com/library/JJ542503(v=VS.85).aspx) | Defines the interface for a XAML object reference manager. Implement this interface to manage instances of [**IReferenceTracker**](https://msdn.microsoft.com/library/JJ542495(v=VS.85).aspx) on XAML objects. |
| [**IReferenceTrackerTarget**](https://msdn.microsoft.com/library/JJ542508(v=VS.85).aspx) | Defines an interface implemented by a garbage collector object referenced from XAML. |
| [**IRestrictedErrorInfo**](/windows/desktop/api/RestrictedErrorInfo/nn-restrictederrorinfo-irestrictederrorinfo) | Represents the details of an error, including restricted error information. |
| [**ISoftwareBitmapNative**](/windows/desktop/api/windows.graphics.imaging.interop/nn-windows-graphics-imaging-interop-isoftwarebitmapnative) | Represents a software bitmap. |
| [**ISoftwareBitmapNativeFactory**](/windows/desktop/api/windows.graphics.imaging.interop/nn-windows-graphics-imaging-interop-isoftwarebitmapnativefactory) | Creates instances of [**ISoftwareBitmapNative**](/windows/desktop/api/windows.graphics.imaging.interop/nn-windows-graphics-imaging-interop-isoftwarebitmapnative). |
| [**IStorageFolderHandleAccess**](/windows/desktop/api/windowsstoragecom/nn-windowsstoragecom-istoragefolderhandleaccess) | Provides access to the operating system handle of a storage folder. |
| [**IStorageItemHandleAccess**](/windows/desktop/api/windowsstoragecom/nn-windowsstoragecom-istorageitemhandleaccess) | Provides access to the operating system handle of a storage file. |
| [**IStringable**](https://msdn.microsoft.com/library/Dn302135(v=VS.85).aspx) | Provides a way to represent the current object as a string. |
| [**ISurfaceImageSourceManagerNative**](/windows/desktop/api/windows.ui.xaml.media.dxinterop/nn-windows-ui-xaml-media-dxinterop-isurfaceimagesourcemanagernative) | Enables performing bulk operations across all [**SurfaceImageSource**](https://msdn.microsoft.com/library/Hh702041(v=WIN.10).aspx) objects created in the same process. |
| [**ISurfaceImageSourceNativeWithD2D**](/windows/desktop/api/windows.ui.xaml.media.dxinterop/nn-windows-ui-xaml-media-dxinterop-isurfaceimagesourcenativewithd2d) | Provides the implementation of a shared Microsoft DirectX surface which is displayed in a [**SurfaceImageSource**](https://msdn.microsoft.com/library/Hh702041(v=WIN.10).aspx) or [**VirtualSurfaceImageSource**](https://msdn.microsoft.com/library/Hh702050(v=WIN.10).aspx). |
| [**ISurfaceImageSourceNative**](/windows/desktop/api/windows.ui.xaml.media.dxinterop/nn-windows-ui-xaml-media-dxinterop-isurfaceimagesourcenative) | Provides the implementation of a shared fixed-size surface for Direct2D drawing. |
| [**ISuspendingDeferral**](isuspendingdeferral.md) | Manages a delayed app suspending operation. |
| [**ISuspendingEventArgs**](isuspendingeventargs.md) | Provides data for an app suspending event. |
| [**ISuspendingOperation**](isuspendingoperation.md) | Provides information about an app suspending operation. |
| [**ISwapChainBackgroundPanelNative**](/windows/desktop/api/windows.ui.xaml.media.dxinterop/nn-windows-ui-xaml-media-dxinterop-iswapchainbackgroundpanelnative) | Provides interoperation between XAML and a DirectX swap chain. |
| [**ISwapChainPanelNative**](/windows/desktop/api/windows.ui.xaml.media.dxinterop/nn-windows-ui-xaml-media-dxinterop-iswapchainpanelnative) | Provides interoperation between XAML and a DirectX swap chain. Unlike [**SwapChainBackgroundPanel**](https://msdn.microsoft.com/library/Hh702626(v=WIN.10).aspx), a **SwapChainPanel** can appear at any level in the XAML display tree, and more than 1 can be present in any given tree. |
| [**ISwapChainPanelNative2**](/windows/desktop/api/windows.ui.xaml.media.dxinterop/nn-windows-ui-xaml-media-dxinterop-iswapchainpanelnative2) | Provides interoperation between XAML and a DirectX swap chain. Unlike [**SwapChainBackgroundPanel**](https://msdn.microsoft.com/library/Hh702626(v=WIN.10).aspx), a **SwapChainPanel** can appear at any level in the XAML display tree, and more than 1 can be present in any given tree. |
| [**ITypedEventHandler<TSender, TArgs>**](https://msdn.microsoft.com/library/Hh438424(v=VS.85).aspx) | Represents the method that will handle an event from a sender of type **TSender** and event data of type **T**. |
| [**IUnbufferedFileHandleOplockCallback**](/windows/desktop/api/windowsstoragecom/nn-windowsstoragecom-iunbufferedfilehandleoplockcallback) | Defines a callback method that you want to run when the opportunistic lock for a handle that you get by calling the [**IUnbufferedFileHandleProvider::OpenUnbufferedFileHandle**](/windows/desktop/api/windowsstoragecom/nf-windowsstoragecom-iunbufferedfilehandleprovider-openunbufferedfilehandle) method is broken. |
| [**IUnbufferedFileHandleProvider**](/windows/desktop/api/windowsstoragecom/nn-windowsstoragecom-iunbufferedfilehandleprovider) | Provides access to handles from a random-access byte stream that the [**StorageFile.OpenAsync**](https://msdn.microsoft.com/library/BR227221(v=Win.10).aspx) method created. |
| [**IVector<T>**](https://msdn.microsoft.com/library/BR224590(v=VS.85).aspx) | Represents a random-access collection of elements. |
| [**IVectorChangedEventArgs**](ivectorchangedeventargs.md) | Provides data for a [**VectorChanged**](https://msdn.microsoft.com/library/BR226053(v=Win.10).aspx) event. |
| [**IVectorView<T>**](https://msdn.microsoft.com/library/BR224594(v=VS.85).aspx) | Represents an immutable view into a [**IVector(T)**](https://msdn.microsoft.com/library/BR206631(v=Win.10).aspx). |
| [**IVideoFrameNative**](/windows/desktop/api/windows.media.core.interop/nn-windows-media-core-interop-ivideoframenative) | Represents a frame of video data. |
| [**IVideoFrameNativeFactory**](/windows/desktop/api/windows.media.core.interop/nn-windows-media-core-interop-ivideoframenativefactory) | Creates instances of [**IVideoFrameNative**](/windows/desktop/api/windows.media.core.interop/nn-windows-media-core-interop-ivideoframenative). |
| [**IViewProvider**](https://msdn.microsoft.com/library/Hh438426(v=VS.85).aspx) | Represents a view in an application. |
| [**IViewProviderFactory**](https://msdn.microsoft.com/library/Hh438427(v=VS.85).aspx) | Creates an instance of views that implement the [**IViewProvider**](https://msdn.microsoft.com/library/Hh438426(v=VS.85).aspx) interface. |
| [**IVirtualSurfaceImageSourceNative**](/windows/desktop/api/windows.ui.xaml.media.dxinterop/nn-windows-ui-xaml-media-dxinterop-ivirtualsurfaceimagesourcenative) | Provides the implementation of a large (greater than the screen size) shared surface for DirectX drawing. |
| [**IVirtualSurfaceUpdatesCallbackNative**](/windows/desktop/api/windows.ui.xaml.media.dxinterop/nn-windows-ui-xaml-media-dxinterop-ivirtualsurfaceupdatescallbacknative) | Provides an interface for the implementation of drawing behaviors when a [**VirtualSurfaceImageSource**](/windows/desktop/api/windows.ui.xaml.media.dxinterop/nn-windows-ui-xaml-media-dxinterop-ivirtualsurfaceimagesourcenative) requests an update. |
| [**IWeakReference**](https://msdn.microsoft.com/library/BR224608(v=VS.85).aspx) | Represents a weak reference to an object. |
| [**IWeakReferenceSource**](https://msdn.microsoft.com/library/BR224609(v=VS.85).aspx) | Represents a source object to which a weak reference can be retrieved. |
| [**MapChangedEventHandler<K, V>**](https://msdn.microsoft.com/library/BR224612(v=VS.85).aspx) | Represents the method that handles the [**MapChanged**](https://msdn.microsoft.com/library/BR226051(v=Win.10).aspx) event of an observable map. |
| [**VectorChangedEventHandler<T>**](https://msdn.microsoft.com/library/BR224626(v=VS.85).aspx) | Represents the method that handles the [**VectorChanged**](https://msdn.microsoft.com/library/BR226053(v=Win.10).aspx) event of an observable vector. |