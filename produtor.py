from confluent_kafka import Producer

# definições para execução cluster kafka local
conf={
    'bootstrap.servers':'localhost:9092',
    'client.id': 'python-producer'
}

# cria o produtor
producer = Producer(conf)

# nome do tópico
topic = 'meu_topico'

def delivery_callback(err, msg):
    if err is not None:
        print(f"Erro ao enviar mensagem: {err}\n")
    else:
        print(f"Mesagem enviada com sucesso!\n")

# envia mensagem e exibe status da operação
while True:
    msg = input("Digite sua mensagem (ou 'x' para sair'): ")
    if msg =='x':
        break

    try:
        producer.produce(topic, key='chave', value=msg, callback = delivery_callback)
        
        producer.flush()
    except Exception as e:
        print(f"Erro ao tentar envias a mensagem:\n{e}\n")
        
# encerra produtor caso a opção digitada seja x
producer.close()
