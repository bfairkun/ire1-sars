rule DownloadBams:
    output:
        bam = "all_bams/{sample}.bam",
        bai = "all_bams/{sample}.bam.bai",
    params: lambda wildcards: samples.loc[wildcards.sample]['Link']
    shell:
        """
        wget -O {output.bam} {params}
        samtools index {output.bam}
        """
