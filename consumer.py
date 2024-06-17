from confluent_kafka import Consumer, KafkaError

conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'python-consumer-group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(conf)
topic = 'meu_topico'

consumer.subscribe([topic])

try:
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue

        if msg.error():
            print(f"Erro na recepção da mensagem: {msg.error()}")
            # Adicione lógica para lidar com o erro, como tentar reconectar
            continue

        print(f"Mensagem recebida em meu_topico: {msg.value().decode('utf-8')}")

except KeyboardInterrupt:
    print("Interrompido pelo usuário")
except Exception as e:
    print(f"Erro geral: {e}")

finally:
    # Fecha o consumidor
    consumer.close()