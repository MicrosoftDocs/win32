---
description: The primary component of the printing interface is the print spooler.
ms.assetid: 36ffb001-78e2-4fa0-8241-3891493ac02d
title: Print Spooler
ms.topic: article
ms.date: 05/31/2018
---

# Print Spooler

The primary component of the printing interface is the print spooler. The print spooler is an executable file that manages the printing process. Management of printing involves retrieving the location of the correct printer driver, loading that driver, spooling high-level function calls into a print job, scheduling the print job for printing, and so on. The spooler is loaded at system startup and continues to run until the operating system is shut down.

Applications that print create a printer device context (DC). When an application creates a printer DC, the spooler performs necessary tasks such as determining the location of the required printer driver and then loading that driver. The print spooler also determines the data type used to record the print job.

The print spooler supports the following data types:

-   Enhanced metafile (EMF).
-   ASCII text.
-   Raw data, which includes printer data types such as PostScript, PCL, and custom data types.

Custom data types can be added to the spooler by installing additional printer drivers and print processors. A print job is a document stored internally and encoded by using one of the supported data types, and a print job may contain one or more pages of output. The print job may consist of multiple forms; for example, a job may consist of one envelope and three pages of A4 paper. A print job is defined (or bracketed) by the [**StartDoc**](/windows/desktop/api/Wingdi/nf-wingdi-startdoca) and [**EndDoc**](/windows/desktop/api/Wingdi/nf-wingdi-enddoc) functions.

The default data type for a print job is the enhanced metafile. An EMF record is a compact structure used to store text output commands, raster graphics commands, and so on. When an application calls [**StartDoc**](/windows/desktop/api/Wingdi/nf-wingdi-startdoca), the spooler creates a spool file and a data file and begins storing EMF records in the spool file. Each time the application calls one of the GDI drawing functions, one or more new EMF records are created and stored in the spool file. The spool and data files are created in an operating system directory. The spooler uses the spool file to store EMF records and uses the data file to record the type of form, the data type for the print job, the target printer, and so on. The spooler deletes these files when the job has successfully printed.

## Related topics

<dl> <dt>

[Enhanced-Format Metafiles](/windows/desktop/gdi/enhanced-format-metafiles)
</dt> </dl>

 

 
