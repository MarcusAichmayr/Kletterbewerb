python set_data.py

declare -a documents=("routenzettel" "laufzettel" "etiketten" "urkunden")

EXPORT_DIR=generated/documents/
if [ ! -e "$EXPORT_DIR" ]
then
    mkdir -p "$EXPORT_DIR"
fi

cd latex
for document in "${documents[@]}"
do
    cd "$document"
    pdflatex "$document".tex
    pdflatex "$document".tex
    cp "$document".pdf "../../"$EXPORT_DIR
    cd ..
done

echo "Generierte PDFs sind in $EXPORT_DIR."
