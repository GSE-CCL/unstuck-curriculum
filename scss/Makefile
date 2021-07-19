#Compiles Bootstrap sass to css; output written to site css folder. 

modules := bootstrap style strategies
distdir := ../app/static/css/

sources := $(addsuffix .scss,$(modules))
outputs := $(addsuffix .css,$(addprefix $(distdir),$(modules)))
mapfiles := $(addsuffix .css.map,$(addprefix $(distdir),$(modules)))

$(distdir)%.css : %.scss
	sass $< $@

all: $(outputs)

.PHONY: clean 
clean:
	-rm $(outputs) $(mapfiles)
