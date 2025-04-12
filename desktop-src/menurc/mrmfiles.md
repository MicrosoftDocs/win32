---
title: File resources in MRM
description: Description of file resources in MRM.
keywords:
- MrmIndexFile MrmIndexFileAutoQualifiers MrmIndexEmbeddedData MrmIndexResourceContainerAutoQualifiers
ms.topic: concept-article
---

# File resources in MRM

File resources in MRM are essentially the same as String resources, except that at runtime the
[**ResourceCandidate.Kind** property](/windows/windows-app-sdk/api/winrt/microsoft.windows.applicationmodel.resources.resourcecandidate.kind) will be **Path** instead of **String**. The resource values are just strings - the 
file names - and not the actual file contents. In fact, in most cases the files being indexed do not even need 
to exist at build time.

If your target application will be using the built-in MRT runtime
([**Windows.ApplicationModel.Resources**](/uwp/api/windows.applicationmodel.resources)), you can use
[**ResourceCandidate.GetValueAsFileAsync**](/uwp/api/windows.applicationmodel.resources.core.resourcecandidate.getvalueasfileasync)
or [**ResourceCandidate.GetValueAsStreamAsync**](/uwp/api/windows.applicationmodel.resources.core.resourcecandidate.getvalueasstreamasync)
to automatically locate and load the file for you. If you are using the WinApp SDK version of MRT 
([**Microsoft.Windows.ApplicationModel.Resources**](/windows/windows-app-sdk/api/winrt/microsoft.windows.applicationmodel.resources)) then
it you must manually load the file yourself. You can also choose to manually load the file with the buit-in MRT
runtime.

There are two ways to add files to the MRM indexer:

* [**MrmIndexFile**](mrmindexfile.md) is the most general and flexible function.
* [**MrmIndexFileAutoQualifiers**](mrmindexfileautoqualifiers.md) automatically infers both the resource 
name and qualifiers from the file name.

Note that [**MrmIndexResourceContainerAutoQualifiers**](mrmindexresourcecontainerautoqualifiers.md) does not 
add a file resource to the indexer; instead it loads the named file at build-time and copies the embedded 
resources to the indexer directly. 

For an alternate to referencing files by name, you can use [**MrmIndexEmbeddedData**](mrmindexembeddeddata.md) 
to embed data directly in the PRI file - see **Embedded data** below for more info.

## Naming files

The primary purpose of file-based resource is to pass a string to functions such as **CreateFile()**, **fopen()**,
or the **std::fstream** constructor. Because the final on-disk path of the files is typically not known at
build time, file names are usually relative paths that will be resolved against the app's working directory
(or some other well-known directory) at runtime. Although it is possible to include any arbitrary string
as the filename (including absolute or network paths), this is typically not useful. 

### Project Root and relative file names

When creating an indexer via one of the **MrmCreateIndexer...** functions, you must specify a *projectRoot* parameter.
This parameter is used by **MrmIndexResourceContainerAutoQualifiers** to locate the files on-disk to parse, and
by **MrmIndexFileAutoQualifiers** to compute relative paths from absolute paths. It is ignored by
**MrmIndexFile**.

## Embedded data

Embedding files as data can reduce the storage space required for your app and increase its performance
relative to referencing filenames. Nevertheless, there are some drawbacks to using this feature, particularly 
during inner-loop app development.

On a typical Windows system, every file wastes an average of 2kb of disk space due to the way disk space 
is allocated. For apps that contain lots of small files (like icons), this average can be even higher. 
By embedding the binary file data directly in the PRI file, this per-file space is not wasted.

Furthermore, loading external resource files is slower than reading binary data directly out of the PRI file, 
since every file open operation requires additional disk accesses, security checks, and so on.
The PRI file is always loaded as a memory-mapped file, so accessing the data is faster.

Despite these benefits, using embedded binary data has limitations, particularly during inner-loop development:

* Build times are increased, as the files containing the binary data need to be loaded and added to the indexer.
Adding file-based resources requires no additional disk access at build time (the disk access is 
deferred until runtime).
* Debugging issues with the PRI file (via XML dumps) is harder, since instead of human-readable filenames 
the XML dump will contain BASE64-encoded binary data. Additionally, the XML dump files will be significantly
larger, making debugging any issues harder.
* Since the contents of the files are embedded directly in the PRI file, it is no longer possible to swap
out assets on-the-fly. Any change to any embedded resource will require a full rebuild of the PRI file.
Since file-based resources only include the filename, the actual asset files can be updated at any time.
* For packaged apps, the image resources listed in the AppXManifest - such as Start Menu icons - cannot be 
embedded and *must* be specified as file resources.

For theses reasons, a general rule of thumb is to use file-based resources during inner-loop development,
but consider using embedded binary resources for final production builds (except for the Manifest resources).
For packaged apps, consider placing the AppXManifest resources (such as Start Menu icons) in a separate 
directoy from other resources to simplify the build process (AppXManifest resources are added as files,
and other resources added as embedded data).
