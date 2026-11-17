
import joblib

modelo = joblib.load("bug_classifier.joblib")


def classificar_bug(descricao, limite_confianca=0.70):

    if not isinstance(descricao, str) or not descricao.strip():
        raise ValueError("Informe uma descrição válida.")

    probabilidades = modelo.predict_proba([descricao])[0]

    indice_maior = probabilidades.argmax()

    categoria = modelo.classes_[indice_maior]

    probabilidade = probabilidades[indice_maior]

    status = (
        "Classificação automática"
        if probabilidade >= limite_confianca
        else "Necessita de análise humana"
    )

    return {
        "descricao": descricao,
        "categoria": categoria,
        "probabilidade": round(float(probabilidade) * 100, 2),
        "status": status
    }


if __name__ == "__main__":

    descricao = "O pagamento via Pix não foi confirmado"

    resultado = classificar_bug(descricao)

    print(resultado)
