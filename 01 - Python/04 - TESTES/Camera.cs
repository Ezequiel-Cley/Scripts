using UnityEngine;

public class CameraFollow : MonoBehaviour
{
    public Transform target; // Referência ao personagem
    public float smoothSpeed = 0.125f; // Velocidade de suavização
    public Vector3 offset; // Deslocamento da câmera

    void LateUpdate()
    {
        if (target != null)
        {
            Vector3 desiredPosition = target.position + offset; // Posição desejada
            Vector3 smoothedPosition = Vector3.Lerp(transform.position, desiredPosition, smoothSpeed); // Suavização
            transform.position = smoothedPosition; // Atualiza a posição
        }
    }
}
