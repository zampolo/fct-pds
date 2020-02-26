pds-01-apresentacao.pdf: pds-01-apresentacao.ps
	ps2pdf pds-01-apresentacao.ps

pds-01-apresentacao.ps: pds-01-apresentacao.dvi
	dvips pds-01-apresentacao.dvi

pds-01-apresentacao.dvi: pds-01-apresentacao.tex
	latex pds-01-apresentacao.tex
	latex pds-01-apresentacao.tex

clean:
	rm *.aux *.dvi *.log *.ps *.toc *.bm
