---
description: The TRANSFORMS property is a list of the transforms that the installer applies when installing the package.
ms.assetid: 'da20f99e-3022-4382-97bb-8f1206072347'
title: TRANSFORMS property
ms.topic: article
ms.date: 05/31/2018
---

# TRANSFORMS property

The **TRANSFORMS** property is a list of the transforms that the installer applies when installing the package. The installer applies the transforms in the same order as they are listed in the property. Transforms can be specified by their filename or full path. To specify multiple transforms, separate each file name or full path with a semicolon (;). For example, to apply three transforms to a package, set **TRANSFORMS** to a list of file names or to a list of full paths.

``` syntax
TRANSFORMS=transform1.mst;transform2.mst;transform3.mst
TRANSFORMS=\\server\share\path\transform1.mst;\\server2\share2\path2\transform2.mst;\\server3\share3\path3\transform3.mst
```

You can indicate that a transform file is embedded in a storage of the .msi file, rather than as a stand-alone file, by prefixing the filename with a colon (:). For example, the following example indicates that transform1.mst and transform2.mst are embedded inside the .msi file and that transform3.mst is a stand-alone file.

``` syntax
TRANSFORMS=:transform1.mst;:transform2.mst;transform3.mst
```

The installer requires the transforms listed in **TRANSFORMS** at every installation, advertisement, installation-on-demand, or maintenance installation of the package. The [TransformsSecure policy](transformssecure-policy.md) policy, the **TRANSFORMS** property, and the first character of the **TRANSFORMS** string informs the installer how to handle the source resiliency of stand-alone transform files. Windows Installer treats setting [TransformsAtSource policy](transformsatsource-policy.md) or [**TRANSFORMSATSOURCE**](transformsatsource.md) the same as TransformsSecure policy and [**TRANSFORMSSECURE**](transformssecure.md). Note that transforms embedded in the .msi file are not cached and are always obtained from the package.




| TRANSFORMS Property | Transforms Secure | Caching and Resiliency | 
|---------------------|-------------------|------------------------|
| @[<em>list of filenames</em>] Example:<br /> @transform1.mst;transform2.mst; transform3.mst<br /> | No effect. | <a href="secure-at-source-transforms.md">Secure-At-Source transforms</a>. The source of the transforms must be at the root of the source for the package. When the package is installed or advertised, the installer saves the transforms on the user's computer in a cache where the user does not have write access. If the local copy of the transform becomes unavailable, the installer searches for a source to restore the cache. The method is the same as searching the source list for an .msi file. See <a href="source-resiliency.md">Source Resiliency</a>. | 
| |[<em>list of paths</em>] Example:<br /><pre class="syntax" data-space="preserve"><code>|\\server\share\path\transform1.mst;\\server2\share2\path2\transform2.mst</code></pre> | No effect. | <a href="secure-full-path-transforms.md">Secure-Full-Path transforms</a>. The source of each transform must be at the full path passed to <strong>TRANSFORMS</strong>. The transform source does not have to be located at the source of the package. When the package is installed or advertised, the installer saves the transforms on the user's computer in a cache where the user does not have write access. If the local copy of the transform becomes unavailable the installer can only restore the cache from the source at the specified path. | 
| [<em>list of filenames</em>] The first character is not @ or |.<br /> Example:<br /> transform1.mst;transform2.mst; transform3.mst<br /> | <a href="transformssecure-policy.md">TransformsSecure policy</a> or <a href="transformssecure.md"><strong>TRANSFORMSSECURE</strong></a> set to 1 OR<br /><a href="transformsatsource-policy.md">TransformsAtSource policy</a> or <a href="transformsatsource.md"><strong>TRANSFORMSATSOURCE</strong></a> set to 1.<br /> | If <strong>TRANSFORMS</strong> is a list of filenames, the installer treats them as <a href="secure-at-source-transforms.md">Secure-At-Source transforms</a>. If <strong>TRANSFORMS</strong> is a list of full paths, the installer treats them as <a href="secure-full-path-transforms.md">Secure-Full-Path transforms</a>.<br /> | 
| [<em>list of filenames</em>] The first character is not @ or |.<br /> Example:<br /> transform1.mst;transform2.mst; transform3.mst<br /> | <a href="transformssecure-policy.md">TransformsSecure policy</a> and <a href="transformssecure.md"><strong>TRANSFORMSSECURE</strong></a> are not set AND<br /><a href="transformsatsource-policy.md">TransformsAtSource policy</a> and <a href="transformsatsource.md"><strong>TRANSFORMSATSOURCE</strong></a> are not set.<br /> | <a href="unsecured-transforms.md">Unsecured Transforms</a>. The source of the transforms must be at the root of the source for the package. When the package is installed or advertised per-user, the installer saves the transforms in the user's profile. This enables a user to roam between computers while maintaining their customizations. For a per-machine install, the transform is saved in the %windir%\Installer folder. If the local copy of the transform becomes unavailable the installer searches for a source to restore the cache. The method is the same as searching the source list for an .msi file. See <a href="source-resiliency.md">Source Resiliency</a>. | 
| [<em>list of paths</em>] The first character is not @ or |.<br /> Example:<br /><pre class="syntax" data-space="preserve"><code>\\server\share\path\transform1.mst;\\server2\share2\path2\transform2.mst.</code></pre> | <a href="transformsatsource-policy.md">TransformsAtSource policy</a> and <a href="transformssecure.md"><strong>TRANSFORMSSECURE</strong></a> are not set AND<br /><a href="transformsatsource-policy.md">TransformsAtSource policy</a> and <a href="transformssecure.md"><strong>TRANSFORMSSECURE</strong></a> are not set..<br /> | <a href="unsecured-transforms.md">Unsecured Transforms</a>. When the package is installed or advertised per-user, the installer saves the transforms in the user's profile. This enables a user to roam between computers while maintaining their customizations. For a per-machine install, the transform is saved in the %windir%\Installer folder. If the local copy of the transform becomes unavailable, the installer searches for a source to restore the cache. The method is the same as searching the source list for an .msi file. See <a href="source-resiliency.md">Source Resiliency</a>. | 




 

You cannot use filenames and paths together in the same **TRANSFORMS** list. You cannot specify secure and profile transforms together in the same list. You may include transforms embedded in the package in a list with other transforms.

``` syntax
@transform1.mst;:transform2.mst 
|\\server\share\path\transform1.mst;:transform2.mst
```

Note that because the list delimiter for transforms is the semicolon character, semicolons must not be used in a transform filename or path.

## Remarks

In cases where the [TransformsSecure policy](transformssecure-policy.md) or the [**TRANSFORMSSECURE**](transformssecure.md) property has been set with Windows Installer, it is not necessary to pass the @ or \| symbol when setting **TRANSFORMS** using the command line. The installer assumes Secure-At-Source or Secure-Full-Path if the list consists entirely of file names located at the source or consists entirely of full paths. You still cannot mix the two types of transform sources.

Note that the installer uses a different search order for unsecured transforms applied during first time and maintenance installations. For more information, see [Unsecured Transforms](unsecured-transforms.md).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> <dt>

[Database Transforms](database-transforms.md)
</dt> <dt>

[Merges and Transforms](merges-and-transforms.md)
</dt> <dt>

[Source Resiliency](source-resiliency.md)
</dt> </dl>

 

 




