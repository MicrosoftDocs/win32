---
description: The recommended method for generating a patch package is to use patch creation tools such as Msimsp.exe and Patchwiz.dll. The Msimsp.exe tool is only available in the Windows SDK Components for Windows Installer Developers.
ms.assetid: fa8e9d68-3db1-4d17-aa99-2ca0ed421c7a
title: Msimsp.exe
ms.topic: article
ms.date: 05/31/2018
---

# Msimsp.exe

The recommended method for generating a patch package is to use patch creation tools such as Msimsp.exe and [Patchwiz.dll](patchwiz-dll.md). The Msimsp.exe tool is only available in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md).

Msimsp.exe is a executable file that calls [Patchwiz.dll](patchwiz-dll.md). The tool can be used to create a patch package by passing in the path to a patch creation properties file (.pcp file) and the path to the patch package that is being created. Msimsp.ex can also be used to create a log file and to specify a temporary folder in which the transforms, cabinets, and files that are used to create the patch package are saved.

The command-line syntax for Msimsp.exe is:

**Msimsp.exe -s** *\[path to .pcp file\]* **-p** *\[path to .msp file\]* **{options}**

The command-line options are not case-sensitive, and slash delimiters can be used instead of a dash. If no options are specified, Msimsp.exe displays the current values of the summary Information properties.

<dl> <dt>

<span id="-s_path_to_.pcp_file_"></span><span id="-S_PATH_TO_.PCP_FILE_"></span>**-s***\[path to .pcp file\]*
</dt> <dd>

This is required and must be followed by the path to the patch creation properties file (.pcp extension). For more information, see [PatchWiz.dll](patchwiz-dll.md).

</dd> <dt>

<span id="-ppath_to_.msp_file"></span><span id="-PPATH_TO_.MSP_FILE"></span>**-p***path to .msp file*
</dt> <dd>

This is required and followed by the path to patch package that is being created (.msp extension).

</dd> <dt>

<span id="-fpath_to_temporary_folder"></span><span id="-FPATH_TO_TEMPORARY_FOLDER"></span>**-f***path to temporary folder*
</dt> <dd>

Optional. Followed by path to temporary folder. The default location is %TMP%\\~pcw\_tmp.tmp\\.

</dd> <dt>

<span id="-k"></span><span id="-K"></span>**-k**
</dt> <dd>

Optional. Fail if the temporary folder already exists.

</dd> <dt>

<span id="-lpath_to_log_file"></span><span id="-LPATH_TO_LOG_FILE"></span>**-l***path to log file*
</dt> <dd>

Optional. Followed by the path to the log file that describes the patch creation process and errors. For more information, see [Return Values for UiCreatePatchPackage](return-values-for-uicreatepatchpackage.md).

</dd> <dt>

<span id="-lppath_to_log_file_with_performance_data"></span><span id="-LPPATH_TO_LOG_FILE_WITH_PERFORMANCE_DATA"></span>**-lp***path to log file with performance data*
</dt> <dd>

Optional. Followed by the path to the log file that describes the patch creation process and errors. This option writes performance data to log file. This option requires version 4.0 of Patchwiz.dll.

</dd> <dt>

<span id="-d"></span><span id="-D"></span>**-d**
</dt> <dd>

Optional. Displays a dialog if the patch creation completes successfully.

</dd> <dt>

<span id="-_"></span>**-?**
</dt> <dd>

Displays command-line help.

</dd> </dl>

> [!Note]
> Msimsp.exe can fail when it calls Makecab.exe if there are values in the File column of the [File table](file-table.md) of the installation package that differ only by case. Windows Installer is case-sensitive and allows an installation package such as in the table below only when Comp1 and Comp2 are installed into different directories. However, in this scenario you cannot use Msimsp.exe or [Patchwiz.dll](patchwiz-dll.md) to generate a patch for the package, because Msimsp.exe and Patchwiz.dll call Makecab.exe, which is case-insensitive.
> 
> Avoid authoring an installation package such as the following partial [File table](file-table.md).
> 
> | File       | Component\_ | FileName   |
> |------------|-------------|------------|
> | readme.txt | Comp1       | readme.txt |
> | ReadMe.txt | Comp2       | readme.txt |


## Related topics

<dl> <dt>

[Creating a Patch Package](creating-a-patch-package.md)
</dt> <dt>

[A Small Update Patching Example](a-small-update-patching-example.md)
</dt> <dt>

[Windows Installer Development Tools](windows-installer-development-tools.md)
</dt> <dt>

[Released Versions, Tools, and Redistributables](released-versions-tools-and-redistributables.md)
</dt> </dl>

 

 



